// Research helper: capture YouTube player timedtext (caption) responses for a video.
import puppeteer from "puppeteer-core";
import fs from "fs";

const [vid, outDir, startSec = "6293"] = process.argv.slice(2);
fs.mkdirSync(outDir, { recursive: true });
const b = await puppeteer.connect({ browserURL: "http://localhost:9222", defaultViewport: null });
const page = await b.newPage();
let n = 0;
page.on("response", async (r) => {
  const u = r.url();
  if (!u.includes("/api/timedtext")) return;
  try {
    const body = await r.text();
    n++;
    fs.writeFileSync(`${outDir}/player-timedtext-${n}.body`, body);
    fs.appendFileSync(`${outDir}/player-timedtext-urls.txt`, `${n}\t${r.status()}\t${body.length}\t${u}\n`);
  } catch (e) { fs.appendFileSync(`${outDir}/player-timedtext-urls.txt`, `${n}\tERR ${e}\t${u}\n`); }
});
await page.goto(`https://www.youtube.com/watch?v=${vid}&t=${startSec}s`, { waitUntil: "domcontentloaded" });
await new Promise((r) => setTimeout(r, 8000));
const info = await page.evaluate(() => {
  const p = document.getElementById("movie_player");
  const out = {};
  try { p.playVideo(); } catch {}
  try { p.mute(); } catch {}
  try { p.loadModule("captions"); } catch {}
  try { out.tracklist = p.getOption("captions", "tracklist"); } catch (e) { out.err1 = String(e); }
  try { out.current = p.getOption("captions", "track"); } catch (e) { out.err2 = String(e); }
  try {
    const pr = window.ytInitialPlayerResponse || p.getPlayerResponse();
    out.captionTracks = pr?.captions?.playerCaptionsTracklistRenderer?.captionTracks?.map((t) => ({ lang: t.languageCode, kind: t.kind, name: t.name?.simpleText || t.name?.runs?.map(r=>r.text).join(""), vssId: t.vssId, url: t.baseUrl }));
  } catch (e) { out.err3 = String(e); }
  return out;
});
// Ensure Vietnamese captions are on
await page.evaluate(() => {
  const p = document.getElementById("movie_player");
  try { p.setOption("captions", "track", { languageCode: "vi" }); } catch {}
});
await new Promise((r) => setTimeout(r, 10000));
const after = await page.evaluate(() => {
  const p = document.getElementById("movie_player");
  return { current: (() => { try { return p.getOption("captions", "track"); } catch (e) { return String(e); } })(),
           shown: Array.from(document.querySelectorAll(".ytp-caption-segment")).map((e) => e.textContent),
           time: p.getCurrentTime?.() };
});
fs.writeFileSync(`${outDir}/player-state.json`, JSON.stringify({ info, after, captured: n, at: new Date().toISOString() }, null, 2));
console.log(JSON.stringify({ captured: n, tracks: info.captionTracks?.map((t) => [t.lang, t.kind, t.name, t.vssId]), current: after.current, shown: after.shown, time: after.time }));
await page.close();
await b.disconnect();
