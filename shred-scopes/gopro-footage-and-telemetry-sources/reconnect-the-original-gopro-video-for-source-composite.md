# How to Reconnect the Original GoPro Video for Source Composite

Saved GoPro telemetry contains measurements and timing, but it does not contain the original video's pixels or audio. Source Composite needs both the active telemetry and the matching original video, so a local source must be reconnected when Studio was opened from a saved extraction.

## When reconnection is required

Reconnect the source when:

- A saved Telemetry Library item was loaded into Studio
- A previous browser session no longer has access to the local file
- The source drive was disconnected and later restored
- Studio asks for the source before opening or rendering Source Composite

A standalone telemetry-overlay export does not require source pixels. Reconnection is specifically required when the GoPro image or audio must be part of the output.

## 1. Locate the exact original file

Before opening Source Composite, locate the original GoPro recording that produced the active telemetry.

Use the file copied directly from the camera or its memory card. Do not use:

- A rendered edit
- A social-media download
- A proxy file
- A transcoded copy
- A neighboring clip with a similar camera filename

Keep the source drive connected and available throughout preview and export.

## 2. Load the saved telemetry

Open [Shred Scopes](https://shredscopes.com/) on a desktop computer, sign in, and select "Studio."

Choose "Choose Metadata from Account" and select the intended extraction, or open it from "Manage Media" > "Telemetry Library."

Confirm the record's name, duration, and available streams before attaching a video.

## 3. Select the source video

When Studio shows that the active telemetry has no attached video:

1. Select "Select Source Video."
2. Browse to the exact original GoPro clip.
3. Select the file.
4. Keep the page open while Studio validates and prepares it.

Studio reports that it is validating the selection. Do not switch to a different clip or reload the page during this check.

## 4. Confirm a successful link

When the file is accepted, Studio reports that the source video is linked. Source Composite becomes available once the video is ready.

Open Source Composite and verify:

- The source video appears in the preview.
- The telemetry changes at the expected moments.
- The timeline duration is correct.
- Source audio is present when expected and supported.
- Overlay graphics remain synchronized near the beginning and end.

Inspect several distinct events, such as a stop, turn, acceleration, altitude change, or jump, rather than judging synchronization from a single frame.

## 5. Arrange and export the composite

After the source is linked:

1. Add or select the telemetry templates required for the finished video.
2. Position and scale them over the source preview.
3. Check readability across representative frames.
4. Set the intended timeline range.
5. Review video and audio export settings.
6. Export the completed Source Composite file.

Keep the original source available until export completes.

## If the source is rejected

Studio can display a message beginning "Selected video does not match the loaded telemetry" when the chosen file does not correspond to the active extraction.

If that occurs:

1. Cancel the current selection.
2. Recheck the telemetry record's source or custom name.
3. Locate the original camera file associated with that record.
4. Select "Select Source Video" again.
5. Choose the corrected file.

Do not attempt to force a similar clip into the project. Even footage from the same camera, recording mode, and outing can have different timing and telemetry.

If the original was renamed, use duration, creation time, neighboring camera filenames, and stored project notes to identify it. Renaming does not necessarily make the file invalid, but selecting the correct underlying recording is essential.

## `.360` source limitation

Saved telemetry extracted from an original `.360` file can drive templates and standalone overlay exports. The `.360` source video itself cannot be previewed or rendered in Source Composite.

For that footage, export the telemetry overlay separately and combine it with rendered or reframed 360 video in a compatible editor.

## Result

The saved telemetry and its matching local GoPro video are linked for the current Studio workflow. Source Composite can now use the recording's frames and audio while the saved measurements drive the telemetry graphics.
