# How to Import Telemetry from Multiple GoPro Clips

The "Import GoPro Clips" page can process multiple original GoPro files as a queue and save their parsed telemetry to the Telemetry Library. Each file is extracted and reported separately, so one failure does not make the entire selection indistinguishable.

The original videos remain on the local device. Only the extracted telemetry records are saved to the account.

## Before starting

Gather the original MP4 or `.360` GoPro clips and keep them on an available local drive. The import page does not list MOV as an accepted format; open a MOV through Studio's standard single-clip source picker instead.

For a large selection:

- Connect the computer to power.
- Keep the browser page open and visible.
- Avoid disconnecting the camera card or source drive.
- Allow time for local extraction and account saving.
- Use a stable network connection for the save stage.

## 1. Open the multi-clip import workflow

Open [Shred Scopes](https://shredscopes.com/) on a desktop computer and sign in.

Then:

1. Open "Manage Media."
2. Select "Import GoPro Clips."
3. Drag the source files onto "Drop GoPro clips," or select "Choose MP4 or 360 clips."
4. Choose two or more original GoPro files.

The selected files appear in an import queue.

## 2. Add an optional batch name

Enter a value in "Batch name" when the clips belong to the same activity, date, location, or project.

A useful batch name should make the group recognizable later without replacing the identity of each source. Examples include an event name, trail name, trip, or recording date.

The field is optional. Leave it blank when no group label is needed.

## 3. Let the queue process

Keep the import page open while Shred Scopes works through the files. Each item passes through its own local extraction and save stages.

The time required depends on:

- Number of selected files
- Individual clip sizes and durations
- Amount of recorded telemetry
- Local storage speed
- Computer performance
- Connection speed during account saving

Do not close the tab after the first file completes. Later queue items may still be extracting, parsing, identifying, or saving.

## 4. Read the per-file results

Review the status shown for every source. Common completed states include:

- "Upload complete" when the parsed telemetry was saved
- "Upload skipped" when the item was recognized as a duplicate and did not need another saved copy

A skipped duplicate is not the same as an extraction failure. Check the Telemetry Library for the existing record before attempting to import it again.

Failed items remain identifiable in the queue. Use the error information to determine whether the source file, telemetry, local access, account access, or connection caused the problem.

## 5. Retry eligible failures

Use "Retry" on an individual failed item after correcting its condition. Use "Retry Failed" when several failed items can be attempted again together.

Before retrying:

- Confirm that the original source drive is still connected.
- Confirm that the file can still be read locally.
- Restore a stable network connection if saving was interrupted.
- Replace re-encoded copies with original GoPro files.
- Leave successful and duplicate-skipped items unchanged.

Retrying only the failed work avoids repeating already completed saves.

## 6. Review the saved library

After the queue finishes, select "View Library" or open "Telemetry Library" from Manage Media.

Confirm that each expected extraction appears. Library records can be renamed with a custom name to distinguish clips whose camera filenames are similar.

When an item provides "Load in Editor," use it to open that telemetry in Studio. Otherwise, open the saved record from the Telemetry Library.

## 7. Understand what the queue saved

Each saved item contains parsed telemetry rather than a copy of the original video. This distinction affects later work:

- The saved record can drive template previews and standalone telemetry exports.
- The saved record can be opened without extracting the source again.
- Source Composite still needs the exact original video associated with that record.
- The original source file must remain in the user's own storage.

For imported `.360` footage, the telemetry remains usable for templates, but the `.360` video cannot be rendered in Source Composite.

## Multi-clip import checklist

Before leaving the page, confirm that:

- Every intended item shows a successful or understood duplicate status.
- Failed items have been retried or intentionally left unresolved.
- Expected records appear in the Telemetry Library.
- The original GoPro files remain safely stored for later Source Composite use.
- The batch name and any custom library names make the sources identifiable.

## Result

The Telemetry Library contains reusable telemetry extractions from the completed queue. The files can now be opened individually for template work without processing the entire selection again.
