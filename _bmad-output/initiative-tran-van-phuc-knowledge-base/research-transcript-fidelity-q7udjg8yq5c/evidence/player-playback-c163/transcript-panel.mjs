// Research helper: open YouTube's "Show transcript" panel and dump all segments.
import puppeteer from "puppeteer-core";
import fs from "fs";
const [vid, out] = process.argv.slice(2);
const b = await puppeteer.connect({ browserURL: "http://localhost:9222", defaultViewport: null });
const page = await b.newPage();
await page.setViewport({ width: 1400, height: 900 });
const gt = [];
page.on("response", async (r) => { if (r.url().includes("get_transcript")) { try { gt.push(await r.text()); } catch {} } });
await page.goto(`https://www.youtube.com/watch?v=${vid}`, { waitUntil: "domcontentloaded" });
await new Promise((r) => setTimeout(r, 9000));
await page.evaluate(() => document.getElementById("movie_player")?.pauseVideo());
const clicked = await page.evaluate(async () => {
  const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
  document.querySelector("#description-inline-expander #expand, tp-yt-paper-button#expand")?.click();
  await sleep(1500);
  const cands = [...document.querySelectorAll("ytd-video-description-transcript-section-renderer button, button")];
  const btn = cands.find((e) => /transcri|chép lời|bản ghi/i.test((e.textContent || "") + (e.getAttribute("aria-label") || "")));
  if (btn) { btn.click(); return (btn.textContent || btn.getAttribute("aria-label")).trim(); }
  return null;
});
await new Promise((r) => setTimeout(r, 8000));
const segs = await page.evaluate(() => [...document.querySelectorAll("ytd-transcript-segment-renderer, transcript-segment-view-model")].map((e) => e.innerText.replace(/\s+/g, " ").trim()));
fs.writeFileSync(out, JSON.stringify({ clicked, n: segs.length, segs, get_transcript_raw: gt }, null, 1));
console.log(JSON.stringify({ clicked, n: segs.length, gt: gt.length }));
await page.close(); await b.disconnect();
