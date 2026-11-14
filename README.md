# Daily Glimmer – weekly long video renderer
Pushing `manifests/<date>.json` renders a 16:9 compilation (vertical Shorts on a blurred background, smooth crossfades between all parts – `transition`/`transition_seconds` in the manifest, default fade 0.8 s) with ffmpeg on GitHub Actions and publishes `out.mp4` + `chapters.txt` as a GitHub Release named `<date>`.

Manifest format:
```json
{"title": "This Week in Good News", "segments": [{"url": "https://…/intro.mp4", "title": "Intro"}, {"url": "https://…/short1.mp4", "title": "Tigers are back"}]}
```
Public download URL of the result: `https://github.com/<owner>/<repo>/releases/download/<date>/out.mp4`

## Glim explainer videos (passthrough)
Push the finished MP4 to `glim/<tag>.mp4` together with `manifests/<tag>.json`:
```json
{"passthrough": true, "title": "Glim explains: …", "file": "glim/<tag>.mp4"}
```
The workflow publishes the file unchanged (no re-encode) as `https://github.com/<owner>/<repo>/releases/download/<tag>/out.mp4`.
