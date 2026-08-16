# How to Cache Extracted GoPro Telemetry While Creating a Video

Studio can optionally save newly extracted GoPro telemetry to the account while a local clip is being prepared for editing. The preference is labeled "Cache telemetry in account."

Caching makes the parsed data available for a later session without uploading the full source video. It does not create an online backup of the GoPro footage.

## When telemetry caching is useful

Enable caching when:

- The same clip will be used in more than one editing session.
- Several template variations will be created from the same telemetry.
- Template work may continue without the original source drive connected.
- Repeating a long extraction should be avoided.
- The telemetry should be available through the account's Telemetry Library.

Leave it disabled when the source is temporary, the extraction should not be retained, or the current project is the only expected use.

## 1. Open Studio and find the preference

Open [Shred Scopes](https://shredscopes.com/) on a desktop computer, sign in, and select "Studio."

At the source-selection stage, locate "Cache telemetry in account." The option appears only when telemetry saving is available to the signed-in account.

If the preference is not present, continue with a local clip for the current session or use an account with access to the feature.

## 2. Enable caching before extraction

Turn on "Cache telemetry in account" before choosing the GoPro clip.

Studio retains this preference for later Studio use in the same browser. Confirm its state at the start of a future project rather than assuming that another device or browser has the same setting.

The preference applies to newly extracted telemetry. Turning it on after a source is already prepared does not necessarily repeat or save the completed extraction.

## 3. Choose the original GoPro source

Select "Choose Clip" and open the original MP4, MOV, or `.360` file.

Keep the page open while Studio:

1. Reads the source locally.
2. Finds and parses its embedded telemetry.
3. Prepares the values used by templates.
4. Saves the parsed telemetry to the account when caching is enabled and available.

The source video's frames and audio remain in the local file. Caching saves the extracted telemetry payload, not the full video.

## 4. Continue creating the video

After extraction, choose a compatible template and continue through the normal Template Editor or Source Composite workflow.

Caching does not change the active source during the current session. The local clip can still provide video frames and audio for Source Composite, except that `.360` source video is not supported in that view.

The cache is a reusable data record, not a different export format and not a substitute for completing the current render.

## 5. Confirm that the telemetry was saved

After the extraction and account save complete:

1. Open "Manage Media."
2. Select "Telemetry Library."
3. Use "Filter Telemetry Library" or page navigation to locate the source.
4. Confirm the source filename or custom name and relevant summary information.

Do not leave the Studio page during an active extraction or save merely to check the library. Wait until preparation has completed.

If no record appears, verify that caching was enabled before the clip was selected and that the account provides telemetry-saving access.

## Load the cached telemetry later

In a later session, open Studio and choose "Choose Metadata from Account," or open the item directly from the Telemetry Library.

The cached record can drive:

- Template preview
- Template customization
- Standalone overlay export

For Source Composite, select "Select Source Video" and reconnect the exact original GoPro file. Studio validates the file before using its pixels and audio with the saved telemetry.

## Caching compared with the import page

Both caching and "Import GoPro Clips" can create saved telemetry records, but they suit different entry points:

- "Cache telemetry in account" accompanies the ordinary Studio workflow while a clip is being opened for editing.
- "Import GoPro Clips" is a separate Manage Media workflow for deliberately preparing and saving one or more sources.

Use caching when saving is incidental to the current creation. Use the import page when building or organizing the Telemetry Library is the primary task.

## Storage and privacy distinction

After caching, two separate items exist:

- The original GoPro video on local storage
- The parsed telemetry record in the Shred Scopes account

Deleting or losing the local video removes the source frames and audio needed for Source Composite, even if the telemetry record remains. Deleting the saved telemetry record does not delete the original local clip.

## Result

The extracted telemetry is retained for later account-backed use while the original GoPro footage stays on the local device. Keep the original file safely stored whenever a future Source Composite export may be required.
