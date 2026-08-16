# How to Load a GoPro Video and Extract Telemetry in Your Browser

Shred Scopes can read an original GoPro clip locally in a desktop browser, extract its embedded telemetry, and make the available data streams usable in animated templates. The source video does not need to be uploaded before editing begins.

This tutorial covers the standard one-clip Studio workflow rather than the separate account import page.

## Before starting

Prepare:

- An original GoPro MP4, MOV, or `.360` file
- A desktop computer
- A current desktop browser
- Enough time for the browser to read and parse the source

Keep the file on an available local drive. If it is stored on removable or network storage, avoid disconnecting that location while Studio is using it.

## 1. Open the Studio source picker

Open [Shred Scopes](https://shredscopes.com/) in the desktop browser, sign in, and select "Studio" from the site navigation.

When no source is active, Studio presents source choices including:

- "Choose Clip" for an original local GoPro video
- "Use Sample Clip" for the included practice source
- "Choose Metadata from Account" for telemetry previously saved to the account

Select "Choose Clip."

## 2. Select the original GoPro file

Choose the file copied from the camera or its memory card. The standard source picker supports MP4, MOV, and `.360` clips.

Do not substitute an edited or downloaded copy merely because it plays correctly. Re-encoding can remove the embedded telemetry while leaving the visible video unchanged.

After selection, keep the Studio page open while the browser prepares the source.

## 3. Wait for local extraction

Studio reads the selected file on the device. It locates the embedded camera metadata, parses the recorded samples, aligns the samples with the video timeline, and prepares values required by the editor.

The source footage itself is not uploaded as part of this step. Processing time can vary with:

- Clip duration and file size
- The number of recorded telemetry samples
- Computer and storage performance
- Browser performance

Do not close or reload the page during extraction. If the browser asks for renewed access to the file, select the same original source.

## 4. Review the extracted result

When preparation finishes, Studio uses the active source to determine which telemetry choices and templates are compatible.

Inspect the available data before choosing a design. Depending on the file, Studio may find values such as:

- Ground speed and 3D speed
- GPS route, coordinates, course, and time
- Altitude, vertical speed, distance, and grade
- Acceleration, camera motion, rotation, and G-force
- In-air state and cumulative airtime
- Elapsed time
- Derived maximum, minimum, cumulative, or rate values

Not every GoPro clip contains every stream. Missing GPS data does not necessarily mean that motion or elapsed-time data is also missing.

## 5. Choose a compatible template

Continue to the template chooser and select a design that uses data present in the active source.

After the Template Editor opens:

1. Play the preview.
2. Scrub to several points on the timeline.
3. Confirm that the displayed values change as expected.
4. Check units, labels, and visual range.
5. If a required value is unavailable, return to the template selection or choose a different recorded stream.

The active source controls the usable telemetry list. Selecting a template does not create a stream that the camera did not record.

## 6. Decide whether to cache the telemetry

If the account provides the option, enable "Cache telemetry in account" before extracting a source when the parsed result should be retained for later use.

Caching stores the extracted telemetry, not the original video. A later session can load the saved data for template work and standalone overlay export. Source Composite still requires the matching original GoPro video because saved telemetry has no source frames or audio.

If the option is disabled, the local source can still be used for the current Studio session without adding the extraction to the Telemetry Library.

## 7. Continue to preview or export

With a compatible template open, the extracted values can drive the Template Editor preview and a standalone telemetry-overlay export.

For a finished video that includes the GoPro image and audio, switch to Source Composite. Keep the original source connected because that workflow needs the local video in addition to its telemetry.

For `.360` sources, use the telemetry for template and standalone-overlay work. The `.360` video itself cannot be previewed or rendered in Source Composite.

## If extraction does not succeed

Check these conditions:

- The file is an original GoPro recording rather than a re-encoded copy.
- The standard source picker received an MP4, MOV, or `.360` file.
- The file still exists at the selected location and the drive remains available.
- The clip contains embedded camera telemetry.
- GPS was recorded if the intended template requires GPS-derived values.
- The browser tab remained open throughout processing.

Try the original file from the camera card if another copy fails. A file that contains no usable embedded telemetry cannot supply values merely by being opened in Studio.

## Result

The GoPro clip is now the active local source. Its extracted streams can animate compatible templates, and its video can also support Source Composite when the source format is previewable. The original file remains under local control unless its parsed telemetry is separately saved to the account.
