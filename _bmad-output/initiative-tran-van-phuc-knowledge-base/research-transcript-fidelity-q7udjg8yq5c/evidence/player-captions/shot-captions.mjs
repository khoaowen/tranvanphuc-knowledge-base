// Research helper: seek YouTube player to given seconds, pause, screenshot the rendered caption.
import puppeteer from "puppeteer-core";
import fs from "fs";
const [vid, outDir, ...secs] = process.argv.slice(2);
const b = await puppeteer.connect({ browserURL: "http://localhost:9222", defaultViewport: null });
const page = await b.newPage();
await page.setViewport({ width: 1280, height: 800 });
await page.goto(`https://www.youtube.com/watch?v=${vid}&t=${secs[0]}s`, { waitUntil: "domcontentloaded" });
await new Promise((r) => setTimeout(r, 8000));
await page.evaluate(() => { const p = document.getElementById("movie_player"); p.mute(); p.playVideo(); p.loadModule("captions"); p.setOption("captions", "track", { languageCode: "vi" }); });
const res = [];
for (const s of secs) {
  await page.evaluate((t) => { const p = document.getElementById("movie_player"); p.seekTo(Number(t), true); p.playVideo(); }, s);
  await new Promise((r) => setTimeout(r, 3500));
  const st = await page.evaluate(() => { const p = document.getElementById("movie_player"); p.pauseVideo(); return { t: p.getCurrentTime(), shown: Array.from(document.querySelectorAll(".ytp-caption-segment")).map((e) => e.textContent) }; });
  const el = await page.$("#movie_player");
  const f = `${outDir}/screen-${s}.png`;
  await el.screenshot({ path: f });
  res.push({ requested: s, ...st, file: f });
}
fs.writeFileSync(`${outDir}/screens.json`, JSON.stringify(res, null, 2));
console.log(JSON.stringify(res.map((r) => [r.requested, r.t.toFixed(1), r.shown.join(" / ")])));
await page.close(); await b.disconnect();
