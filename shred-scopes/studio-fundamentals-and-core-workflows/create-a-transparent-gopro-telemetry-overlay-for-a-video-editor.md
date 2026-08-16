# How to Create a Transparent GoPro Telemetry Overlay for a Video Editor

A transparent telemetry overlay contains animated GoPro data without the original footage or an opaque background. It can be placed on a video track above the source clip in software such as Adobe Premiere Pro or DaVinci Resolve.

Shred Scopes creates this output from the Template Editor. Source Composite is not required because the source footage will be added later in the finishing application.

## Choose a transparency-capable format

Shred Scopes provides three overlay formats that can preserve an alpha channel:

| Format | Typical use |
| --- | --- |
| PNG-codec MOV | High-quality transparent frames in a MOV container for compatible editing software |
| QuickTime Animation MOV | A qtrle alpha MOV for compatible post-production workflows |
| WebM | A VP9 or VP8 alpha export when supported by the browser encoder and destination software |

H.264 MP4 does not preserve transparency. The Template Editor can export an H.264 overlay over a solid color, but that background must be removed with a chroma-key effect in the video editor.

Check the destination application's format support before rendering a long or high-resolution overlay.

## 1. Load telemetry in Studio

Open [Shred Scopes](https://shredscopes.com/) in a supported desktop browser, sign in, and select "Studio."

Choose one of the available telemetry sources:

- "Choose Clip" to read telemetry from an original GoPro file
- "Choose Metadata from Account" to use a saved telemetry extraction
- "Use Sample Clip" to practice with supplied footage and data

The original source video is not required when saved telemetry already exists and only the standalone overlay will be exported.

## 2. Open or create the overlay template

Select a built-in or custom template. The Template Editor opens after the telemetry and template are ready.

Confirm the following before export:

- The template uses streams available in the source.
- The unit system is correct.
- Text and graphics remain inside the template canvas.
- The design has sufficient contrast for the footage used in the final edit.
- The animation behaves correctly throughout the required timeline range.

The checkerboard around or behind a template represents transparency in the editing workspace. Layers can still contain their own opaque fills, images, or backgrounds, so inspect the template rather than assuming every part of the canvas is transparent.

## 3. Set the required timeline range

Use the timeline playhead to inspect the source. If only part of the telemetry is needed, set the in and out points for the intended segment.

Choose "Rebuild data graphics from range" when the overlay contains a GPS path, automatic data range, elapsed time, distance, cumulative altitude, cumulative airtime, or another range-dependent value that should begin or scale from the selected in point.

Record the chosen range or source timecode when the overlay must align with a specific section of the video in the finishing application.

## 4. Configure the overlay export

Locate the "EXPORT" settings in the Template Editor sidebar and select the required alpha-capable format.

Choose the export size:

- Full size exports the template at its canvas dimensions.
- Half size exports at 0.5 times the canvas dimensions.
- Quarter size exports at 0.25 times the canvas dimensions.

Use full size for the final output unless a smaller graphic is intentionally required. Half or quarter size can reduce the time and storage required for a test render.

Enable "Preserve source timecode" if the overlay must carry the GoPro clip's timecode into a compatible finishing workflow. WebM exports do not provide this option.

## 5. Export the transparent overlay

Select "Export" in the top toolbar and choose a destination when prompted. Keep the Studio tab open and visible until rendering finishes.

After export, verify:

- The file opens in the destination editor.
- Its frame size matches the intended sequence or placement.
- Its duration matches the selected range.
- Its animation aligns with the original source footage.
- The alpha channel is recognized by the destination application.

If the finishing application does not recognize the file's transparency, confirm that an alpha-capable format was selected and that the application supports that codec and container combination.

## 6. Place the overlay in the video editor

Import the original GoPro video and the exported overlay into the editing project. Place the source footage on a lower video track and place the telemetry overlay directly above it.

Align the files using their starting points, recorded timecode, or the range used during export. Avoid changing the speed of only one item because the displayed telemetry would no longer correspond to the source frames.

The overlay can be repositioned or scaled in the finishing application, but exporting it at an appropriate canvas size from Shred Scopes preserves more flexibility and image quality.

## Transparent overlay or keyed MP4

Use an alpha-capable MOV or WebM when the destination workflow supports it. Use the keyed-background H.264 MP4 only when transparency is unavailable or a chroma-key workflow is specifically required.

For a finished file that already includes the GoPro video and audio, return to Studio and use Source Composite instead of exporting the template by itself.
