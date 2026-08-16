# Local GoPro Clip vs Saved Telemetry vs Sample Clip in Shred Scopes

Studio can begin with an original local GoPro clip, a saved telemetry extraction, or an included sample clip. All three can supply data to telemetry templates, but they do not provide the same video, audio, storage, or Source Composite capabilities.

Choose the source that matches the intended task before opening a template.

## Source comparison

| Capability | Local GoPro clip | Saved telemetry | Sample clip |
| --- | --- | --- | --- |
| Represents personal footage | Yes | Yes, as extracted data | No |
| Requires telemetry extraction when selected | Yes | No | No user extraction required |
| Includes access to original source frames | Yes, while the local file is linked | No | Included for practice |
| Includes source audio | Yes, when present and supported | No | Included sample behavior only |
| Drives compatible template previews | Yes | Yes | Yes |
| Supports standalone overlay export | Yes | Yes | Intended primarily for practice |
| Supports Source Composite | Yes, except `.360` source video | Only after linking the matching original clip | Available for learning the workflow |
| Retained in the account | Only if extracted telemetry is cached or imported | Yes | Supplied by Shred Scopes |

Open [Shred Scopes](https://shredscopes.com/) on a desktop computer, sign in, and select "Studio" to see the available source choices.

## Choose a local GoPro clip for the complete workflow

Select "Choose Clip" when the original GoPro file is available on the device.

Studio reads the file locally and prepares its embedded telemetry. This source provides the broadest workflow because it can supply:

- Recorded telemetry for template animation
- Video frames for Source Composite
- Source audio when present and supported
- Source timing information when present

A local clip is the appropriate choice when the goal is a finished Source Composite video or when the telemetry extraction has not yet been saved.

Keep the original file available throughout editing and export. Moving, renaming, disconnecting, or deleting it can require the source to be selected again.

An original `.360` clip can supply telemetry, but its video cannot be previewed or rendered in Source Composite.

## Choose saved telemetry for account-backed template work

Select "Choose Metadata from Account" when the required extraction already exists in the Telemetry Library.

Saved telemetry can:

- Drive compatible template previews
- Support template editing and customization
- Support standalone telemetry-overlay export
- Avoid repeating extraction from the source file
- Be renamed, opened, and managed from the Telemetry Library

Saved telemetry does not contain the original video's pixels or audio. It is not a cloud copy of the GoPro clip.

To use Source Composite after loading saved telemetry, select "Select Source Video" and choose the matching original GoPro file. Studio verifies the file before linking it to the active telemetry.

## Choose the sample clip for practice

Select "Use Sample Clip" when learning Studio without personal footage.

The sample can be used to:

- Explore built-in templates
- Learn the Template Editor and Source Composite layouts
- Practice timeline playback and scrubbing
- Test common customization controls
- Review the export setup without first locating a personal source

Treat the sample as a practice source rather than a prediction of personal footage. A personal GoPro clip may have different streams, duration, frame rate, aspect ratio, motion, GPS coverage, and value ranges.

Work created against the sample should be checked again after the intended GoPro source is loaded.

## Choose by intended output

### For a finished video containing source footage

Use the original local GoPro clip. If saved telemetry is loaded first, reconnect the exact original clip before opening Source Composite.

### For a separate transparent or keyed overlay

Use either a local clip or saved telemetry. Both can drive a standalone telemetry export when the required streams are available.

### For template design without the source file nearby

Use saved telemetry. The design can later be checked against the original video after the matching source is linked.

### For learning the interface

Use the sample clip. Replace it with the intended source before making final compatibility, range, or placement decisions.

## What happens when the source changes

The active source determines the available streams and the values seen by templates. Changing from the sample to personal footage, or from one saved extraction to another, can affect:

- Which stream choices are available
- Whether an existing data mapping remains compatible
- Minimum and maximum values used by gauges
- Route and graph shape
- Timeline duration
- Placement decisions in Source Composite

After changing the source, review all open templates across the full timeline. Studio can mark a previously selected stream unavailable when the new source does not contain it.

## Practical selection rule

Use the local original when video frames or audio are needed, saved telemetry when account-backed data is sufficient, and the sample when the task is practice. Do not treat saved telemetry as a replacement for the original file or treat the sample's telemetry coverage as representative of every GoPro recording.
