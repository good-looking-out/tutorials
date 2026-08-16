# Which GoPro Video Files Can You Use in Shred Scopes?

Shred Scopes reads telemetry embedded in original GoPro video files and uses that data to create animated gauges, maps, graphs, and other telemetry graphics. The file must be compatible with the selected workflow, and it must still contain the telemetry recorded by the camera.

The filename extension alone does not confirm that a clip contains usable telemetry.

## Accepted source files in Studio

The standard single-clip source picker in Studio accepts:

- MP4 files
- MOV files
- GoPro `.360` files

To open the source picker, visit [Shred Scopes](https://shredscopes.com/) on a desktop computer, sign in, select "Studio," and choose "Choose Clip."

Use an original file copied from the GoPro whenever possible. A compatible extension does not restore telemetry that was removed by another application.

## Accepted files on the Import GoPro Clips page

The separate "Import GoPro Clips" page accepts original MP4 and `.360` GoPro files. It does not list MOV as an import format.

This difference matters when choosing a workflow:

- Use Studio's "Choose Clip" option to work directly with one MP4, MOV, or `.360` source.
- Use "Import GoPro Clips" to extract and save telemetry from one or more MP4 or `.360` clips in the Telemetry Library.

If a MOV file is the available source, open it through the standard Studio source picker instead of the import page.

## Use the original camera file

GoPro telemetry is stored inside the camera's video container. Copies produced by other services or applications may retain the visible video while discarding the telemetry track.

Avoid using these as the source when the original is available:

- A clip exported from a video editor
- A social-media download
- A file sent through a messaging service that recompresses video
- A screen recording
- A proxy or optimized-media copy
- A file converted to another codec or container

Renaming a re-encoded file with an MP4, MOV, or `.360` extension does not restore its telemetry. Return to the file copied directly from the camera or memory card.

## Confirm that the camera recorded the required data

A valid GoPro file can contain some telemetry streams without containing every stream supported by Shred Scopes. Availability depends on the camera, recording mode, camera settings, and conditions during recording.

For example:

- GPS-based speed, position, route, distance, course, and altitude require recorded GPS data.
- A camera with GPS support generally needs GPS enabled and a usable satellite lock while recording.
- Motion streams depend on data recorded by the camera's sensors.
- Derived values are available only when their required source measurements are present.

A clip can therefore be usable for a G-force design while lacking a GPS route, or usable for elapsed-time graphics while lacking GPS speed.

## Understand the `.360` limitation

Shred Scopes can extract telemetry from a compatible original `.360` file and use that data for telemetry templates and standalone overlay exports.

However, `.360` source video cannot be previewed or rendered in Source Composite. Source Composite requires ordinary source frames that Studio can place behind the telemetry graphics. For `.360` footage, export the telemetry graphic separately and combine it with reframed or rendered footage in a compatible video editor.

## Check a file in Studio

1. Open Shred Scopes on a desktop browser.
2. Sign in and select "Studio."
3. Choose "Choose Clip."
4. Select the original MP4, MOV, or `.360` file.
5. Wait for extraction and parsing to finish.
6. Review the telemetry streams and compatible template choices that become available.

If Studio reports that telemetry cannot be found, verify the source before assuming that the extension is unsupported.

## Troubleshooting checklist

When a clip is rejected or expected data is missing, check the following:

- The file came directly from the GoPro or its memory card.
- The selected workflow accepts that file format.
- The file was not transcoded, repaired, or exported by another application.
- The recording mode and camera model support the expected sensor data.
- GPS was enabled and had a satellite lock if a GPS-based graphic is required.
- The file is stored on an available local drive and can be read by the browser.

If only one telemetry type is missing, inspect the other available streams. The file may still support templates that do not depend on the absent data.

## File-choice summary

Use an original MP4, MOV, or `.360` file for the standard single-clip Studio workflow. Use original MP4 or `.360` files for the separate import workflow. Regardless of extension, verify the telemetry found in the active source before selecting a template or planning an export.
