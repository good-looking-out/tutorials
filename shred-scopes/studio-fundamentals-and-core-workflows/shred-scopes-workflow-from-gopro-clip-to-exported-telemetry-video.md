# The Shred Scopes Workflow: From GoPro Clip to Exported Telemetry Video

The Shred Scopes workflow consists of four broad stages: selecting source material, preparing telemetry, building or choosing a graphic, and exporting video. Several decisions within those stages determine whether the result is a standalone overlay, a finished Source Composite, or a multi-file batch.

This tutorial maps the complete process rather than prescribing one template or export format.

## Stage 1: Prepare the recording and browser

Shred Scopes works from telemetry embedded in compatible GoPro files. An original camera file is the preferred source because processed copies often lose the telemetry track.

For the broadest support, use a current desktop Chromium-based browser such as Chrome, Edge, Brave, or Opera. Editing is not supported on phones or tablets. Batch Mode additionally depends on Chromium directory-write support.

Before starting, confirm that there is enough free storage for the expected export. Transparent MOV files can be substantially larger than delivery-oriented MP4 files.

Open [Shred Scopes](https://shredscopes.com/), sign in, and select "Studio" from the navigation.

## Stage 2: Choose the source type

Studio provides three source paths.

### Original GoPro clip

Select "Choose Clip" to read telemetry from a local GoPro file. This path can provide telemetry, video frames, audio, source dimensions, frame rate, and timecode where those tracks are available.

Choose one clip for a standard workflow. Selecting two or more clips can start Batch Mode.

### Saved telemetry

Select "Choose Metadata from Account" to load telemetry previously saved to the account. This avoids repeating extraction and supports template editing and standalone overlay export.

Saved telemetry does not contain source frames or audio. Link the matching original file with "Select Source Video" before entering Source Composite.

### Sample clip

Select "Use Sample Clip" to learn the editor or test a design without personal footage. A sample provides its own telemetry and video characteristics; it does not predict which streams or dimensions another GoPro file will contain.

## Stage 3: Prepare the telemetry

When an original clip is selected, Studio reads its embedded telemetry locally in the browser. It then exposes the streams found in that recording.

Available data can include speed, GPS position and path, altitude, distance, heading, grade, vertical speed, acceleration, G-force, camera motion, GPS time, elapsed time, and airtime. The precise list is source-dependent.

At this point, decide whether to save the extraction. With full access, "Cache telemetry in account" can retain the prepared data for future use. The preference is optional and does not upload the original GoPro footage.

## Stage 4: Choose a template

After telemetry is ready, Studio presents the template picker. Select:

- A built-in design for a ready-made starting point
- A custom template already saved to the account
- A new blank template when a design will be built from the beginning

Check compatibility between the selected design and the active telemetry. A GPS path template requires recorded GPS positions; an altitude or speed design requires its corresponding stream.

Many built-in templates provide separate imperial and metric variants. Unit-agnostic designs can be used without selecting a measurement system.

## Stage 5: Edit in the Template Editor

The Template Editor is the Studio workspace for the individual telemetry graphic. It contains the layer controls, canvas, template actions, export settings, preview playback, and timeline.

A template can be modified by:

- Adding, removing, grouping, or reordering layers
- Moving, resizing, rotating, or aligning elements
- Mapping data text, graphics, and ticks to telemetry streams
- Converting measurements into the required units
- Changing colors, fills, strokes, opacity, blend modes, fonts, or images
- Resizing the template canvas

Preview the template at several points on the timeline. Check both ordinary and extreme values so the graphic does not clip, overlap, or become unreadable.

Use "Save" for changes to an existing custom template. Use "Save As New" for a built-in design, a new template, or a separate version.

## Stage 6: Choose the output workflow

There are two standard output paths.

### Standalone overlay

Remain in the Template Editor when the graphic will be placed over footage in another video editor.

Choose an alpha-capable PNG MOV, QuickTime Animation MOV, or supported WebM format for transparency. Choose H.264 MP4 only when a solid chroma-key background is appropriate.

### Source Composite

Select "Composite Mode" when Shred Scopes should place one or more telemetry templates over the original GoPro video and export a finished MP4.

Source Composite provides controls for the output canvas, source fitting and rotation, overlay placement, timeline range, H.264 or HEVC encoding, and video quality. It includes the original source audio in the export.

## Stage 7: Set the timeline range

Use the in and out points to select the required portion of the clip. The complete source remains active unless a shorter range is chosen.

Enable "Rebuild data graphics from range" when the graphic should recalculate for that segment. This affects values such as elapsed time, distance traveled, cumulative airtime, elevation gain or loss, automatic ranges, and range-relative GPS paths.

Confirm the displayed duration before exporting.

## Stage 8: Configure and run the export

For a standalone overlay, select its format, export size, and source-timecode option where available.

For Source Composite, select the canvas dimensions, codec, target bitrate, rate control, encoding priority, hardware preference, keyframe interval, resize sampling, and timecode option as required.

Select "Export" and choose the save destination. Keep the Studio tab open and visible while Shred Scopes renders the video.

When export finishes, verify the file's:

- Duration
- Dimensions
- Telemetry timing
- Visual placement
- Transparency or composited background
- Video and audio playback where applicable

## Stage 9: Retain reusable work

After a successful export, reusable work can be kept in the account:

- Save a custom template for another clip.
- Favorite frequently used templates.
- Save extracted telemetry when it will be used again.
- Review completed and attempted renders in "Export Log."
- Manage custom images used by account templates.

The original GoPro source remains a separate local file. Keep it available when a later Source Composite or source-validation step may be required.

## Standard or Batch Mode

The process above describes one source. For several clips, Batch Mode performs the same general extraction, template, preflight, and export stages per source.

Batch Template Export applies one template to each source and saves the overlay outputs. Batch Source Composite places one or more templates over each local source and saves finished videos. The queue runs sequentially and records success or failure for each item.

## Workflow summary

Every Shred Scopes project can be understood as a sequence:

1. Choose a source.
2. Prepare its telemetry.
3. Choose or build a template.
4. Preview and set the range.
5. Choose standalone overlay or Source Composite.
6. Configure and export the video.
7. Retain any reusable telemetry, templates, images, or export records.

Keeping these stages distinct makes it easier to identify where a source, template, preview, compatibility, or export problem occurs.

