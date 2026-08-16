# How to Create Your First GoPro Telemetry Overlay Video in Shred Scopes

Shred Scopes can turn telemetry recorded inside a compatible GoPro video into an animated overlay. This tutorial covers the basic single-clip workflow for creating and exporting the overlay by itself so it can be placed over footage in a separate video editor.

## Before starting

Prepare the following:

- An original GoPro video containing telemetry
- A desktop computer
- A current Chromium-based browser, such as Chrome, Edge, Brave, or Opera
- A Shred Scopes account with full access if the overlay will be exported
- Enough free storage for the completed video file

The source video remains on the local device. Shred Scopes reads its telemetry and renders the output in the browser.

## 1. Open Studio

Open [Shred Scopes](https://shredscopes.com/) in the desktop browser, sign in, and select "Studio" from the site navigation.

Studio opens at its source picker when no project is active. The main source choices are:

- "Choose Clip" for an original local GoPro file
- "Use Sample Clip" for learning the editor with supplied footage
- "Choose Metadata from Account" for telemetry previously saved to the account

Select "Choose Clip" for this workflow.

## 2. Select the original GoPro video

Choose the original file copied from the GoPro recording. Avoid social-media downloads, transcoded copies, screen recordings, and files exported from a video editor because those versions commonly omit the camera's telemetry track.

Wait while Studio reads the file and prepares its telemetry. The time required depends on the clip's duration, file size, and the computer's performance.

When extraction finishes, Studio makes the telemetry streams found in that file available to compatible templates. The available list can differ from one clip to another.

## 3. Choose a template

Select a template when the "Choose Template" step appears. Built-in templates cover telemetry such as:

- Speed
- Altitude
- Distance
- GPS path
- Grade
- Acceleration
- G-force
- Heading
- Vertical speed

The [public GoPro telemetry overlay template catalog](https://shredscopes.com/gopro-telemetry-overlay-templates) can be used to review designs before entering Studio.

Choose a template whose data is present in the selected clip. If the source lacks a required stream, the corresponding template value can appear unavailable.

## 4. Preview the telemetry animation

The selected design opens in the Template Editor. Use the controls at the bottom of the workspace to inspect it:

1. Select "Play preview" to watch the animation.
2. Drag the timeline playhead to inspect specific moments.
3. Check frames near the beginning, middle, and end of the clip.
4. Confirm that displayed values and units are appropriate.
5. Use the preview zoom control if the canvas is difficult to inspect. Preview zoom does not change the exported dimensions.

Review several points rather than relying on a single frame. A speedometer, route, graph, or cumulative value can behave correctly at one moment but need a different scale or placement elsewhere in the clip.

## 5. Make basic adjustments

A built-in template can be exported without modification, but the Template Editor also allows changes to its layers and appearance.

Common first adjustments include:

- Switching to the required imperial or metric template variant
- Moving or scaling the complete graphic
- Changing text, colors, strokes, or opacity
- Selecting a different compatible telemetry stream
- Converting speed, distance, altitude, or vertical-speed units
- Resizing the template canvas

Built-in template originals are not overwritten. To keep a modified version, open the "Template" menu and use "Save As New". Saving a custom template requires full access.

## 6. Choose the overlay export settings

Use the export settings in the Template Editor sidebar. The main overlay choices are:

- "PNG codec .mov (alpha)" for a high-quality MOV with transparency
- "QuickTime Animation .mov (qtrle alpha)" for another transparency-capable MOV workflow
- "WebM (VP9/VP8 alpha)" when the selected browser encoder supports transparency
- "MP4 (H.264, keyed background)" for a solid-color background that will be removed with a chroma-key effect

For a first transparent overlay, PNG-codec MOV is a direct starting point when the destination editor supports it.

The export-size choices include full, half, and quarter size. Full size matches the template canvas. A smaller scale can be useful for a test render, but confirm that the resulting dimensions are sufficient for the final edit.

Enable "Preserve source timecode" only when the finishing workflow needs the output to retain the source clip's timecode. This option is not available for WebM.

## 7. Export the overlay

Select "Export" in the top toolbar and choose the destination when the browser asks where to save the file.

Keep the Studio tab open and visible until export completes. Moving to another tab or allowing the browser to suspend the page can pause the render until Studio becomes visible again.

After the export finishes, confirm that the output file exists and plays for the expected duration. The overlay can then be placed on a video track above the GoPro footage in a compatible editor.

## Result

The completed file contains the animated telemetry graphic without the original source footage. A transparency-capable export can be placed directly over video; a keyed-background MP4 requires a chroma-key effect in the finishing editor.

When a finished video is needed without a separate editing application, use the Source Composite workflow instead. Source Composite renders one or more telemetry templates over the original GoPro video and exports the combined result.

