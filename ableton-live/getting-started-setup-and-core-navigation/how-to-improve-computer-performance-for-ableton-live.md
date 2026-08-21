# How to Improve Computer Performance for Ableton Live

Clicks, dropouts, slow response, and an overloaded CPU meter indicate that a Live Set needs more processing or disk bandwidth than the computer can provide in real time. Improve performance by checking the audio settings, identifying demanding tracks, and simplifying the Set where it has the greatest effect. The right balance depends on whether you are recording, performing, or mixing in [Ableton Live](https://www.ableton.com/en/live/).

## Video walkthrough

<div class="video-embed">
  <iframe
    src="https://www.youtube-nocookie.com/embed/0dXIa-1N4jI?rel=0"
    title="Learn Live: Computer Performance"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen>
  </iframe>
</div>

## Check the cause before changing settings

Watch Live’s CPU meter and overload indicator while reproducing the problem. Live’s meter describes the pressure on real-time audio processing; it is not the same as the overall CPU percentage shown by macOS Activity Monitor or Windows Task Manager. Use the operating system’s monitor as well to identify competing applications.

In Live 12, show **Performance Impact** indicators from the Mixer controls to find tracks that contribute most to the current Set’s processing load. If the overload indicator shows a disk issue, also check the drive that holds the project and audio files.

## Balance buffer size and latency

Open **Settings > Audio** and adjust the buffer size in small steps.

- Use the lowest stable buffer that gives comfortable monitoring latency when recording or playing instruments.
- Increase the buffer for mixing and editing, when higher latency is acceptable and stable playback is more important.

A smaller buffer requires the computer to process audio more frequently, so it can cause crackles or dropouts in a demanding Set. A larger buffer reduces that demand but increases the delay you feel while monitoring through Live. On some Windows ASIO interfaces, change the buffer in the manufacturer’s control panel instead of Live.

## Use an appropriate sample rate and enabled channels

Set a sample rate that matches the incoming material and the project’s delivery needs. 44.1 kHz and 48 kHz are common starting points. Higher sample rates increase processing demand and will not improve a source recorded at a lower rate.

Disable unused audio inputs and outputs in **Settings > Audio** with **Configure Inputs** and **Configure Outputs**. Keep only the channels needed for the session. This reduces routing clutter and can reduce audio-processing demand.

## Reduce demand in the Set

Start with the tracks identified by Performance Impact indicators. Practical options include:

- Freeze a track with CPU-intensive instruments or effects, then unfreeze it later if changes are needed.
- Reduce instrument polyphony or disable unused effects and devices.
- Replace repeated heavy insert effects with a return track and sends when the mix allows it.
- Use less demanding warp modes where they meet the musical need; several Complex or Complex Pro clips can be costly.
- Close unneeded third-party plug-in windows and confirm that all plug-ins are current and compatible.

Avoid loading two plug-in formats for the same plug-in into one project unless there is a specific need. Test whether a problematic plug-in is responsible by disabling it or its scan location temporarily, then update it rather than relying on an outdated version.

## Protect disk performance and Browser indexing

Keep adequate free space on the system and project drives. Ableton recommends retaining at least 10 percent of the system drive as free space. Use a fast, dependable drive for active projects and audio that must stream during playback.

Add focused content folders to Browser Places. A large drive, Desktop, Downloads, or cloud-synced library can force Live to index unnecessary material. If a spinning indicator appears beside Places after adding content, allow the indexing task to finish before judging Live’s performance.

## Prepare the computer for the task

Update Live, the operating system, audio-interface drivers, MIDI drivers, and plug-ins to versions supported by the computer. Quit resource-heavy applications while working, connect a laptop to power for a demanding session, and prevent overheating. On Windows, use ASIO for a suitable interface and select a high-performance power mode when appropriate.

Treat optimization as a measured process: reproduce the problem, change one factor, and test again. Ableton’s [How to avoid crackles and audio dropouts](https://help.ableton.com/hc/en-us/articles/209070329-How-to-avoid-crackles-and-audio-dropouts), [macOS CPU-load guide](https://help.ableton.com/hc/en-us/articles/5266527910812-Reducing-the-CPU-load-on-macOS), and [Windows CPU-load guide](https://help.ableton.com/hc/en-us/articles/209071269-Reducing-the-CPU-load-on-Windows) provide current platform-specific advice. The source video is [Learn Live: Computer Performance](https://www.youtube.com/watch?v=0dXIa-1N4jI).
