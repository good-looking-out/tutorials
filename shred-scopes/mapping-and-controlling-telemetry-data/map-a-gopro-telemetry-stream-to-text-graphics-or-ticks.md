# How to Map a GoPro Telemetry Stream to Text, Graphics, or Ticks

Data-driven template layers use a telemetry stream to determine what they display at each frame. Shred Scopes can map available GoPro data to changing text, animated graphics, and tick scales while leaving static labels and decorative shapes unchanged.

The active source controls which stream choices are available.

## Understand the data-driven layer types

Use:

- "data·text" to display a changing number, direction, duration, date, or time
- "data·graphic" to animate a gauge, pointer, path, progress bar, chart, or other registered graphic
- "data·ticks" to build a linear or radial scale whose bounds can come from telemetry

A data graphic can expose more than one input. For example, a two-direction G-force dot can use lateral G and longitudinal G separately. Map each input according to its label.

## 1. Load the intended telemetry source

Open [Shred Scopes](https://shredscopes.com/) on a desktop computer, sign in, and select "Studio."

Choose an original GoPro clip, saved telemetry, or a sample. Wait until Studio prepares the source, then open an existing template or start a new one.

Do not design final mappings from the sample alone. A personal source can contain a different set of streams and value ranges.

## 2. Add or select a data layer

To add a layer:

1. Open "Layers."
2. Select "Add Layer" or a plus control labeled "Add layer here."
3. Choose "data·text," "data·graphic," or "data·ticks."
4. Choose the required graphic or tick layout when applicable.
5. Add and rename the layer.

To change an existing mapping, select the layer on the canvas or in the layer list and expand its data or input section.

## 3. Choose the stream

Select "Stream" and choose a compatible source value. Examples include:

- Speed 2D or Speed 3D
- Altitude, vertical speed, distance traveled, or grade
- GPS course, GPS path, or GPS time
- G-force, lateral G, longitudinal G, or camera-axis acceleration
- In-air state, cumulative airtime, or elapsed time
- Running maximum, running minimum, rate, or cumulative altitude variants

The list shows data available from the active source. If a mapping is marked unavailable, load a source that contains it or select another stream.

Choosing a stream does not create measurements that the camera did not record.

## 4. Choose a unit conversion

Use "Convert" when the stream supports the required output unit. Examples include m/s to mph, meters to feet, or m/s² to ft/s².

Apply the same conversion to every related layer. A numeric speed value, gauge, and data-derived ticks should not use different units unless the difference is intentional and clearly labeled.

Update static suffixes and unit labels after conversion.

## 5. Configure the input behavior

Numeric data layers can expose additional controls:

- Smoothing to average rapid visual changes
- "Clamp values" to limit the incoming converted value
- Deadband to hold values near a center at that center
- "Map / normalize input" to fit or map a numeric range
- "Visible when" to show the layer only for a selected data condition

Use only the controls needed for the result. Every added filter or map changes how the selected layer represents the source.

These controls are layer-specific. Another layer mapped to the same stream can use different settings.

## 6. Map text

For data text:

1. Choose the stream and conversion.
2. Select a compatible display format.
3. Set decimal places or duration, direction, date, or time formatting.
4. Add a prefix or suffix when needed.
5. Choose fixed font size or automatic fitting.
6. Position and align the result.

Preview the shortest and longest values. A data-text layer can change width as telemetry changes.

## 7. Map a graphic

For a data graphic:

1. Select the required input stream or streams.
2. Choose conversions.
3. Map the input to the graphic's expected output range when required.
4. Configure geometry and direction.
5. Style the track, progress, pointer, marker, or other visible parts.

For signed movement, verify that positive and negative values drive the expected direction. Use "fit max absolute" or a symmetric fixed range when zero should remain centered.

## 8. Map data ticks

For data linear or radial ticks:

1. Select the same stream and conversion used by the associated graphic.
2. Set "Bounds source" to use telemetry when the scale should adapt.
3. Enable "Include zero" or "Symmetric around zero" when appropriate.
4. Configure major and minor intervals.
5. Style the labels and guide line.

Check that the tick minimum, maximum, and direction agree with the gauge or pointer.

## 9. Preview the animation

Use "Play preview" and scrub to:

- The beginning, middle, and end
- Minimum and maximum values
- Positive and negative events
- Stops or low-motion sections
- Any expected source-data gaps

Confirm that text, graphic movement, ticks, units, and visibility all agree. Rebuild data graphics from the final timeline range when the template uses automatic, cumulative, or range-relative values.

## 10. Save the mapping

Use "Template" > "Save As New" for a built-in template or new version. Use "Save" for changes to an existing custom template.

The layer now converts the selected GoPro stream into the intended text, graphic, or tick behavior for every frame in the active range.
