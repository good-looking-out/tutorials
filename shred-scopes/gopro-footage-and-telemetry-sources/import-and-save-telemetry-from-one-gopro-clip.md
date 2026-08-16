# How to Import and Save Telemetry from One GoPro Clip

The "Import GoPro Clips" workflow extracts telemetry from an original GoPro file in the browser and saves the parsed result to the account's Telemetry Library. The original video remains on the local device and is not stored as part of the telemetry record.

This workflow is useful when telemetry should be available for later template editing without extracting the same clip again.

## Before starting

Prepare:

- An original GoPro MP4 or `.360` file
- A desktop computer and current browser
- A signed-in Shred Scopes account with access to telemetry saving
- A stable connection for saving the extracted result

The import page accepts MP4 and `.360` clips. If the source is a MOV file, use Studio's standard "Choose Clip" workflow instead.

## 1. Open the import page

Open [Shred Scopes](https://shredscopes.com/) on the desktop computer and sign in.

Then:

1. Open "Manage Media."
2. Select "Import GoPro Clips."
3. Locate the area labeled "Drop GoPro clips."

The import page is separate from the main editing workspace. It is intended to prepare account-backed telemetry before or between editing sessions.

## 2. Choose one original clip

Either drag the file onto "Drop GoPro clips" or use "Choose MP4 or 360 clips."

Select the original recording copied from the camera or memory card. An exported, recompressed, or downloaded copy may play normally while lacking the camera's telemetry.

After selection, keep the page open. The browser reads the source locally, extracts the embedded metadata, prepares the telemetry, and creates the information needed to identify the source later.

## 3. Wait for the telemetry review

When extraction finishes, the single-file review displays "Telemetry found" and a source summary. The fields shown depend on the clip and its recorded data, but can include:

- Source filename
- Camera information
- Duration
- Frame rate
- GPS sample counts
- Speed
- Distance
- Ascent and descent
- Jump count

Use this review to confirm that the intended source was selected and that expected measurements were found.

A missing field does not always indicate a failed extraction. Some GoPro files do not contain every supported stream. For example, a recording without usable GPS cannot provide GPS-derived speed or route data.

## 4. Save the extraction

Select "Save to Account" when the review is correct.

Keep the page open while the parsed telemetry is saved. Do not disconnect the network or reload the page during this step.

If the wrong source was selected, choose "Choose Different File" and repeat the extraction with the intended original clip.

Saving adds the parsed telemetry to the account. It does not upload or retain the full GoPro video.

## 5. Open the saved result

After the save completes, use the available action to continue, or return to "Manage Media" and open "Telemetry Library."

From the library, the saved extraction can be:

- Opened in Studio
- Renamed with a custom name
- Used to drive compatible telemetry templates
- Deleted when it is no longer required

Opening saved telemetry avoids repeating extraction, but it does not provide the source video frames or audio.

## 6. Use the telemetry in Studio

Open the saved item in Studio and choose a compatible template. The extraction can support:

- Template preview and customization
- Standalone transparent-overlay export
- Standalone keyed-background overlay export

For Source Composite, select "Select Source Video" and choose the exact original GoPro file used for this extraction. Studio validates the source before making its frames available for compositing.

An imported `.360` source can provide telemetry for template work, but its original `.360` video cannot be previewed or rendered in Source Composite.

## If the import fails

Check that:

- The page received an original MP4 or `.360` GoPro file.
- The file was not exported by a video editor or transcoded.
- The expected telemetry was recorded by the camera.
- The local drive remained connected through extraction.
- The page remained open through extraction and saving.
- The account has access to telemetry saving.

Use "Choose Different File" to select the original camera file when an edited copy fails.

## Result

The Telemetry Library now contains a reusable parsed extraction associated with the original clip. Keep the original GoPro file in a known location because the saved telemetry alone cannot supply source pixels or audio for a future Source Composite export.
