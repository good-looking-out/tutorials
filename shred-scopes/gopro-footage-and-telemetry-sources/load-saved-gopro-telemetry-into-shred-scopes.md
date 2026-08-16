# How to Load Saved GoPro Telemetry into Shred Scopes

Telemetry saved through the import or caching workflow can be reopened without extracting the original GoPro video again. A saved record can drive compatible template previews and standalone overlay exports, but it does not contain the source video frames or audio.

## Before starting

The required extraction must already exist in the account's Telemetry Library. Saved telemetry can be created by:

- Enabling "Cache telemetry in account" before opening a local clip in Studio
- Saving a source through the "Import GoPro Clips" page

Open [Shred Scopes](https://shredscopes.com/) on a desktop computer and sign in to the account that contains the record.

## Method 1: Choose saved telemetry from Studio

When Studio is at its source-selection screen:

1. Select "Choose Metadata from Account."
2. Browse or filter the available saved telemetry.
3. Select the record associated with the required GoPro clip.
4. Wait for Studio to prepare it as the active source.
5. Choose a compatible template.

Use the source filename, custom name, duration, and available summary information to distinguish similar records.

## Method 2: Open a record from the Telemetry Library

Saved telemetry can also be opened from Manage Media:

1. Open "Manage Media."
2. Select "Telemetry Library."
3. Use "Filter Telemetry Library" and page navigation to find the record.
4. Open the item's Studio action.
5. Choose a template if one is not already active.

This method is useful when the library needs to be reviewed or organized before editing begins.

## Verify the selected record

Before making template changes, check that the active telemetry represents the intended source. Compare details such as:

- Source or custom name
- Clip duration
- Frame rate
- Recording or GPS timing when shown
- Available telemetry streams
- Expected speed, distance, altitude, or motion ranges

Two clips from the same activity can have similar camera filenames. Renaming library records with clear custom names can reduce selection errors.

## Choose a compatible template

The saved extraction becomes the active telemetry source. Studio uses its recorded and derived streams to determine the available data choices.

After opening a template:

1. Play the preview.
2. Scrub through the timeline.
3. Confirm that required values are available.
4. Check units and labels.
5. Inspect the beginning, middle, and end for appropriate visual range.

If a design requires a stream absent from the saved extraction, select another compatible template or data mapping. Loading saved telemetry cannot add data that was not present in the original recording.

## Export a standalone telemetry overlay

Saved telemetry can drive the Template Editor's standalone export options. Depending on the chosen format and browser support, the output can be a transparency-capable overlay or a keyed-background file for use in a separate video editor.

Because the export contains the telemetry graphic rather than the source footage, the original GoPro video does not need to remain linked for this workflow.

Keep a copy of the original video for the separate finishing edit and for any future Source Composite work.

## Reconnect video for Source Composite

If Studio reports that no source video is attached, select "Select Source Video" and choose the exact original GoPro clip from which the saved telemetry was extracted.

Studio validates the selected file. When it matches, the source video is linked and Source Composite becomes available after the video is ready.

Do not choose a nearby clip simply because it has a similar name, duration, or recording session. Incorrect source video can produce misaligned telemetry and is rejected when it does not match the active extraction.

An original `.360` file can have saved telemetry, but its source video cannot be previewed or rendered in Source Composite.

## Manage the library record

The Telemetry Library can be used to:

- Assign a clearer custom name
- Reopen the extraction in Studio
- Filter and page through saved items
- Delete a record that is no longer required

Deleting a saved record removes that account-backed extraction. It does not delete the original GoPro file from local storage.

## Result

The saved extraction is now the active Studio source and can animate compatible templates without repeating local telemetry extraction. Reconnect the matching original video only when source frames or audio are required.
