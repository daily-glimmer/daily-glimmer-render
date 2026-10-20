# Daily Glimmer – weekly long video renderer
Pushing `manifests/<date>.json` renders a 16:9 compilation (vertical Shorts on a blurred background) with ffmpeg on GitHub Actions and publishes `out.mp4` + `chapters.txt` as a GitHub Release named `<date>`.

Manifest format:
```json
{"title": "This Week in Good News", "segments": [{"url": "https://…/intro.mp4", "title": "Intro"}, {"url": "https://…/short1.mp4", "title": "Tigers are back"}]}
```
Public download URL of the result: `https://github.com/<owner>/<repo>/releases/download/<date>/out.mp4`
