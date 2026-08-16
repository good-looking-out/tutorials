# How to Check Which Telemetry Streams Are Available Before Choosing a Template

The active GoPro source determines which telemetry values Studio can use. Checking the available streams before choosing or customizing a template prevents a design from depending on data that the camera did not record.

Stream availability can differ between clips from the same camera because GPS lock, camera settings, recording mode, and source-file processing can change what is present.

## 1. Load the intended source

Open [Shred Scopes](https://shredscopes.com/) on a desktop computer, sign in, and select "Studio."

Choose one of the available source types:

- "Choose Clip" for an original local GoPro file
- "Choose Metadata from Account" for a saved extraction
- "Use Sample Clip" for practice

Wait until the source is ready before deciding which production template to use. The sample's streams do not predict what will be available in personal footage.

## 2. Review compatible choices

Continue to the template chooser. Studio uses the active source to make compatible telemetry and template choices available.

After a template opens, select a data-driven text, shape, graph, gauge, or tick layer and inspect its telemetry-stream control. The stream list reflects data available from the active source and values that can be derived from it.

If a required stream is absent, return to a compatible design or change the layer to use an available measurement.

## GPS and position streams

When the source contains sufficient GPS data, available choices can include:

- Ground speed, also described as 2D speed
- 3D speed
- GPS-path acceleration
- Altitude
- Vertical speed
- Distance traveled
- GPS course or direction of travel
- Grade or slope
- Latitude and longitude
- GPS path
- GPS time
- Lateral and longitudinal G derived from the path

These values depend on valid recorded GPS samples. A GoPro model with GPS support still needs the appropriate recording conditions and settings to produce them.

GPS course describes direction of travel. It should not be treated as the physical direction the camera lens is pointing.

## Motion and time streams

Depending on the source, Studio can also provide:

- Camera-axis acceleration on X, Y, and Z
- G-force
- Rotation rate
- In-air state
- Cumulative airtime
- Elapsed time

Motion data and GPS data are separate. A clip can contain motion streams when GPS-derived choices are unavailable.

Elapsed time is based on progress through the active range. GPS time represents recorded clock information when usable GPS timing exists.

## Derived stream variants

Some template choices are calculated from an available base stream. These can include:

- Running maximum
- Running minimum
- Rate of change
- Cumulative distance or airtime
- Cumulative altitude gain
- Cumulative altitude loss

A derived choice is only possible when its required source data exists. For example, elevation gain cannot be produced without usable altitude samples.

Some cumulative and range-dependent values respond to the selected in and out points. Recheck or rebuild the design after changing the active timeline range when Studio indicates that range-dependent data needs updating.

## 3. Check values across the timeline

Do not judge a stream from the first frame alone.

1. Play the preview.
2. Scrub to several positions.
3. Check known events in the footage.
4. Inspect the value range and sign.
5. Confirm that a gauge, graph, or indicator remains readable throughout the clip.

A stream can be present but contain limited useful variation. For example, poor GPS coverage can produce less suitable route or speed behavior even when some GPS samples exist.

## 4. Choose the correct unit and interpretation

After confirming the stream, select the required output unit when the layer supports conversion.

Common choices include:

- Miles per hour or kilometers per hour for speed
- Feet or meters for altitude
- Miles, kilometers, yards, feet, or meters for distance
- Feet per minute or another compatible rate for vertical speed

Unit conversion changes how a value is displayed. It does not create or improve the underlying telemetry.

Also confirm whether the design expects a signed, unsigned, cumulative, or directional value. Longitudinal G, vertical speed, and grade often need a visual range that accommodates both negative and positive values.

## 5. Recheck after changing sources

When a different local clip, saved extraction, or sample becomes active, Studio updates the available stream context. An existing template mapping can become unavailable if the new source lacks its data.

After every source change:

- Inspect data-driven layers for unavailable mappings.
- Review minimum and maximum ranges.
- Check route, graph, and cumulative behavior.
- Confirm the timeline duration.
- Preview the full design again.

Do not assume that two clips from the same activity have identical telemetry coverage.

## If an expected stream is missing

Check that:

- The selected file is the original GoPro recording.
- The camera model and recording mode support the expected data.
- GPS was enabled and had a usable lock for GPS-derived streams.
- The file was not re-encoded or exported by another application.
- The correct saved telemetry record is active.

If the stream was not recorded, choose a template based on the data that is available. Studio cannot reconstruct absent camera measurements merely by changing templates.

## Result

The selected template now uses data confirmed to exist in the active source. Checking availability, value behavior, units, and timeline coverage before export reduces unavailable mappings and misleading telemetry graphics.
