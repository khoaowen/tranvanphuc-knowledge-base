// Research helper: play YouTube from a start time at normal speed (no seeking), sample the rendered
// caption every 250 ms with the player's currentTime, and screenshot every 5 s. Also open the
// "Show transcript" panel and dump its segments near the window.
import puppeteer from "puppeteer-core";
import fs from "fs";
const [vid, outDir, start, dur] = process.argv.slice(2);
fs.mkdirSync(outDir, { recursive: true });
const b = await puppeteer.connect({ browserURL: "http://localhost:9222", defaultViewport: null });
const page = await b.newPage();
await page.setViewport({ width: 1280, height: 800 });
await page.goto(`https://www.youtube.com/watch?v=${vid}&t=${start}s`, { waitUntil: "domcontentloaded" });
await new Promise((r) => setTimeout(r, 9000));
await page.evaluate(() => { const p = document.getElementById("movie_player"); p.mute(); p.playVideo(); p.loadModule("captions"); p.setOption("captions", "track", { languageCode: "vi" }); });
const samples = []; let last = ""; const t0 = Date.now(); let shot = 0;
while (Date.now() - t0 < Number(dur) * 1000) {
  let s;
  try { s = await page.evaluate(() => { const p = document.getElementById("movie_player"); const ad = !!document.querySelector(".ad-showing"); return { t: p.getCurrentTime(), state: p.getPlayerState(), ad, url: location.href, cap: Array.from(document.querySelectorAll(".ytp-caption-segment")).map((e) => e.textContent).join(" / ") }; }); }
  catch (e) { samples.push({ err: String(e).slice(0, 80) }); await new Promise((r) => setTimeout(r, 1000)); continue; }
  if (s.cap !== last || s.ad) { samples.push(s); last = s.cap; }
  if (Date.now() - t0 > shot * 5000) { await (await page.$("#movie_player"))?.screenshot({ path: `${outDir}/play-${s.t.toFixed(1)}.png` }); shot++; }
  await new Promise((r) => setTimeout(r, 250));
}
fs.writeFileSync(`${outDir}/playback-samples.json`, JSON.stringify(samples, null, 2));
// transcript panel
let panel = [];
try {
  await page.evaluate(() => { document.getElementById("movie_player").pauseVideo(); });
  await page.evaluate(() => { const ex = document.querySelector("tp-yt-paper-button#expand, #expand"); ex && ex.click(); });
  await new Promise((r) => setTimeout(r, 1500));
  await page.evaluate(() => { const btn = [...document.querySelectorAll("button, ytd-button-renderer")].find((e) => /transcri|bản chép|transcription/i.test(e.textContent || e.getAttribute("aria-label") || "")); btn && btn.click(); });
  await new Promise((r) => setTimeout(r, 6000));
  panel = await page.evaluate(() => [...document.querySelectorAll("ytd-transcript-segment-renderer")].map((e) => ({ ts: e.querySelector(".segment-timestamp")?.textContent.trim(), text: e.querySelector(".segment-text")?.textContent.trim() })));
} catch (e) { panel = [{ err: String(e) }]; }
fs.writeFileSync(`${outDir}/transcript-panel.json`, JSON.stringify(panel, null, 2));
console.log(JSON.stringify({ samples: samples.length, panelSegments: panel.length }));
await page.close(); await b.disconnect();
