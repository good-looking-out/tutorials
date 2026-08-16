# How Shred Scopes Verifies a Replacement Source Video

When saved telemetry is loaded without its original video, Studio asks for a replacement source before Source Composite can use video frames or audio. Shred Scopes checks that the selected file corresponds to the active telemetry instead of accepting any clip with a similar filename.

This validation protects synchronization between the displayed measurements and the visible action.

## Why a matching source matters

Telemetry values are tied to the timing and content of one recording. A different GoPro clip can have the same resolution, frame rate, and approximate duration while representing different moments.

If unrelated footage were paired with the active telemetry:

- Speed changes could occur at the wrong time.
- GPS position and route progress could be incorrect.
- G-force and acceleration events could be offset.
- Altitude, jump, or airtime displays could describe another recording.
- The source could end before or after the telemetry timeline.

Selecting the original recording is therefore part of maintaining an accurate Source Composite result.

## Start the validation

Open [Shred Scopes](https://shredscopes.com/) on a desktop computer, sign in, and select "Studio."

Load a saved telemetry record, then:

1. Select "Select Source Video."
2. Choose the original local GoPro file associated with the active telemetry.
3. Wait while Studio reports that the source is being validated.
4. Continue only after Studio confirms that the source video is linked.

## What Studio compares

The available comparison information varies with the recording. Studio can use the video's structural details and recorded telemetry characteristics, including:

- Frame rate
- Duration
- Frame count
- Source dimensions
- Video encoding information when present
- Initial GPS timing and position when present
- Samples of position, altitude, speed, GPS time, and motion data when present

These checks are considered together. A filename by itself is not proof of a match, and changing a filename does not turn one recording into another.

The exact set of usable comparisons depends on what the original clip recorded. A source without GPS cannot be checked against GPS characteristics that do not exist, but other timing, video, and motion information can still distinguish files.

## Successful validation

After Studio accepts the file, it reports that the source video is linked. When the video becomes ready, Source Composite can use:

- Original source frames
- Source audio when present and supported
- Active telemetry aligned to the source timeline

Before exporting, preview several identifiable events across the clip. Validation establishes that the file corresponds to the extraction, while visual review confirms that the intended project and template were selected.

## Rejected validation

If the selected file does not match, Studio displays a message beginning "Selected video does not match the loaded telemetry" and does not attach it as the Source Composite video.

Recover by:

1. Reviewing the active telemetry record's source filename or custom name.
2. Checking the original camera card or archive for the associated recording.
3. Comparing duration and recording time with the saved record.
4. Selecting "Select Source Video" again.
5. Choosing the corrected original file.

Do not select a transcoded or trimmed version of the correct recording. Changes to duration, frames, encoding, or embedded data can prevent it from corresponding to the saved extraction.

## Similar files that should not be substituted

Avoid using:

- The preceding or following chapter from the same recording session
- A low-resolution proxy
- A stabilized or color-corrected export
- A clip trimmed to the same approximate duration
- A file from another camera using the same naming pattern
- A social-media or messaging-service copy

Use the original source that produced the telemetry whenever possible.

## Organize files for easier reconnection

To make future validation straightforward:

- Keep original GoPro files in a stable archive.
- Preserve camera filenames or record any renaming.
- Give saved telemetry records descriptive custom names.
- Group related originals by activity and recording date.
- Avoid overwriting originals with edited versions.

The saved telemetry is reusable, but it is not a backup of the corresponding video.

## `.360` files

An original `.360` file can supply saved telemetry, but its source video cannot be previewed or rendered in Source Composite. Use its telemetry for standalone overlay output and finish the 360 video in a compatible application.

## Result

A matching file is linked only after Studio finds sufficient agreement between the selected source and the active extraction. This keeps Source Composite from silently placing valid telemetry over the wrong GoPro recording.
