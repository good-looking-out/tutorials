# How to Use Ableton Link

Ableton Link keeps the beat, tempo, and phase aligned between Link-enabled music applications and hardware on the same local network. It is useful when several devices need to play together without exchanging MIDI clock. Start with [Ableton Live](https://www.ableton.com/en/live/) and at least one Link-enabled peer connected to the same stable Wi-Fi or wired network. The source video uses the Live 10 interface; the steps below use the current Live 12 labels.

## Video walkthrough

<div class="video-embed">
  <iframe
    src="https://www.youtube.com/embed/_Jzz6GKdcFA?rel=0"
    title="Learn Live: Using Ableton Link"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen>
  </iframe>
</div>

## Connect the Link participants to one local network

Connect the computer running Live and every Link-enabled app or hardware device to the same local network. A stable Wi-Fi connection or a wired network connection can be used. Link peers discover one another automatically, so no device address or manual pairing is required.

Enable Link in the settings of each partner app or hardware device. Confirm that the app or device supports Ableton Link; Link-enabled peers can join or leave a session without interrupting the other participants.

Link synchronizes timing, not the ordinary audio path. If a partner device produces audio that you want to hear or record in Live, route that audio to Live separately through your audio interface, or use Link Audio when every relevant device supports it.

## Enable Link in Live and confirm the peers

1. Open Live’s Settings and select **Link**.
2. If the Link control is hidden, set **Show Link Toggle** to show it in the Control Bar. The toggle is displayed there by default.
3. Click the **Link** toggle in the Control Bar to enable Link. Live automatically starts or joins the available Link session.

When other Link-enabled peers are present, the Link toggle displays their number. Open the menu beside the toggle to access Link settings and, when available, information about Link Audio peers.

## Establish tempo and launch in time

The first participant to join a Link session establishes its initial tempo. After that, any participant can change the tempo and the other peers follow it. Avoid changing tempo from more than one device at once, since the most recent change becomes the session tempo.

By default, each participant can start and stop independently while remaining in time and phase with the other peers. When Live is stopped and another peer is connected, the Arrangement Position control shows a progress animation for Live’s global launch quantization. Starting Live waits for the next quantization boundary, which helps the Set enter the shared timing cleanly.

## Share transport start and stop only when needed

To make transport commands travel between devices, enable **Start Stop Sync** in Live’s Link Settings. Enable the corresponding option on every peer that should send or receive those commands; it is not enough to enable the setting on only one device.

With Start Stop Sync active on the participating devices, starting or stopping one can start or stop the others. Leave it disabled when performers need to start and stop their own apps independently while still sharing tempo and phase.

## Use Link Audio as a separate optional workflow

Link Audio extends Link by streaming audio in real time between compatible peers on the same network. In Live 12.4 or later, turn on Link first, then enable **Link Audio** from the Link toggle menu or in Settings. Every device that is meant to exchange audio must have Link Audio enabled.

To monitor or record incoming Link Audio in Live, choose the peer as an audio track’s **Input Type**, choose the source track with **Input Channel**, and set monitoring or record arm as appropriate. This is separate from basic Link synchronization, so a timing-only Link setup does not need Link Audio.

## Avoid conflicts with automation and MIDI sync

Tempo changes received from a Link session override tempo automation in the Live Set. Review any Arrangement tempo automation before connecting a device that may change the shared tempo.

Live can still send regular MIDI data while Link is enabled, but it cannot receive MIDI Sync from an external MIDI source at the same time. Decide whether Link or incoming MIDI clock should be the source of timing before beginning a performance.

Start with two peers, a fixed tempo, and independent transport control. Once both devices stay in phase as expected, add Start Stop Sync or Link Audio only when the setup needs those additional behaviors. This staged approach makes it easier to identify which connection is responsible if synchronization changes unexpectedly.

For current details, see Ableton’s [Synchronizing with Link, Tempo Follower, and MIDI reference](https://www.ableton.com/en/live-manual/12/synchronizing-with-link-tempo-follower-and-midi/), [Link features and functions FAQ](https://help.ableton.com/hc/en-us/articles/209776125-Link-features-and-functions-FAQ), and [Link Audio FAQ](https://help.ableton.com/hc/en-us/articles/25425913328924-Link-Audio-FAQ). The source walkthrough is Ableton’s [Learn Live: Using Ableton Link](https://www.youtube.com/watch?v=_Jzz6GKdcFA).
