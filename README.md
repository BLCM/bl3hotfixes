BL3 Hotfix Archive
==================

This is an archive of the hotfixes which are being sent to Borderlands 3.
The first hotfix data was manually collected on September 21, 2019, and
the next few after that were collected manually as well.  Starting on
October 1, 2019, this project was created to check the hotfix data every
hour and write out the hotfixes automatically.

The hotfixes are written twice: once to a brand-new file which includes
a datestamp, stored in the `point_in_time` directory, and once to
`hotfixes_current.json`.

The script which does this is written in Python 3, and should run anywhere
Python does, though you'll need to edit `output_dir` inside the script
itself to have it save out files properly.  Check `requirements.txt` inside
the script dir for the extra Python modules needed for it to run.

All code in this project is is licensed under the
[New/Modified (3-Clause) BSD License](https://opensource.org/licenses/BSD-3-Clause).
A copy can be found in [COPYING.txt](COPYING.txt).

I've also put up a Google Sheets page which has the *all* of the hotfixes
which have been used by GBX (including ones which are no longer active)
up here: [Combined Hotfixes](https://drive.google.com/open?id=1kfkC2hJs0hZSr12bvrQlY0GyEH4S_KAI_xIAqnGmKnQ).  That sheet has all the fields split out
properly into columns, which can make hotfix investigation a lot easier.

Details
=======

(I'm numbering hotfixes and patches here based on what's officially announced
in the "News" section at borderlands.com, though there have been plenty of
smaller hotfixes/patches which haven't been announced in that area.  Often
it'll just be a tweet, or in a few cases a silent update without any
announcement at all.  A bit silly to keep numbering them, really, but I suppose
I'll continue regardless...)

* **2019-09-13**: Borderlands 3 Initial Release (build version `
  OAK-PADDIESEL1-39-CL-2005984`, reported version `1.0.0 CL 2005984` -
  *confirmation needed for reported version*)
* **2019-09-19**: First announced hotfixes, manually collected on the
  21st.  It's possible there were hotfixes active before this point, but
  these are the first we know of.
  ([GBX Post](https://borderlands.com/en-US/news/2019-09-19-borderlands-3-hot-fixes-sept-19/),
  [Local Post Archive](gbx_info_archive/2019-09-19-hotfixes.md))
* **2019-09-26**: First BL3 patch (build version
  `OAK-PATCHDIESEL-11-CL-2015653`, reported version `1.0.1 CL 2015653`
  *(confirmation needed for reported version)*)
  ([GBX Post](https://borderlands.com/en-US/news/2019-09-26-borderlands-3-patch-sept-26/),
  [Local Post Archive](gbx_info_archive/2019-09-26-patch.md))
* **2019-09-27**: Second announced hotfixes, manually collected on the 27th.
  ([GBX Post](https://borderlands.com/en-US/news/2019-09-27-borderlands-3-hot-fixes-sept-27/),
  [Local Post Archive](gbx_info_archive/2019-09-27-hotfixes.md))
* **2019-10-01**: Week 1 of the Borderlands 10-Year Anniversary Celebration
  begins, with "Boss Week," which increases chances for various bosses to
  drop specific legendary gear.  Manually collected one last time -- any
  hotfixes after this point should be grabbed automatically by this process.
  ([GBX Post](https://borderlands.com/en-US/news/2019-10-01-borderlands-anniversary-celebration/),
  [Local Post Archive](gbx_info_archive/2019-10-01-anniversary_1.md))
* **2019-10-03**: Third announced hotfixes, and second patch (build version
  `OAK-PATCHDIESEL-21-CL-2022342`, reported version `1.0.2 CL 2022342`).
  ([GBX Post](https://borderlands.com/en-US/news/2019-10-03-borderlands-3-patch-hotfixes-oct-3/),
  [Local Post Archive](gbx_info_archive/2019-10-03-patch-and-hotfixes.md))
* **2019-10-05**: Unannounced hotfixes which tweak some level geometry in
  a couple of boss areas, seemingly.
* **2019-10-08**: Week 2 of the Borderlands 10-Year Anniversary Celebration,
  with "Rare Spawn Hunt", after a period of time where Week 1 was disabled but
  Week 2 wasn't active yet.
  ([GBX Post](https://borderlands.com/en-US/news/2019-10-07-borderlands-3-rare-spawn-hunt/),
  [Local Post Archive](gbx_info_archive/2019-10-07-anniversary_2.md))
* **2019-10-10**: Fourth announced hotfixes
  ([GBX Post](https://borderlands.com/en-US/news/2019-10-10-borderlands-3-hotfixes-oct-10/),
  [Local Post Archive](gbx_info_archive/2019-10-10-hotfixes.md))
* **2019-10-15**: Week 3 of the Borderlands 10-Year Anniversary Celebration,
  with "Show Me the Eridium."  A couple of the statements have errors, perhaps
  those will get fixed up eventually.  (They didn't. :)
  ([GBX Post](https://borderlands.com/en-US/news/2019-10-14-borderlands-3-show-me-the-eridium/),
  [Local Post Archive](gbx_info_archive/2019-10-14-anniversary_3.md))
* **2019-10-17**: Fifth announced hotfixes
  ([GBX Post](https://borderlands.com/en-US/news/2019-10-17-borderlands-3-hotfixes-oct-17/),
  [Local Post Archive](gbx_info_archive/2019-10-17-hotfixes.md))
* **2019-10-22**: Week 4 of the Borderlands 10-Year Anniversary Celebration,
  with "Mayhem on Twitch."
  ([GBX Post](https://borderlands.com/en-US/news/2019-10-22-borderlands-3-mayhem-on-twitch/),
  [Local Post Archive](gbx_info_archive/2019-10-22-anniversary_4.md))
* **2019-10-24**: Sixth announced hotfixes, third patch (build version
  `OAK-PATCHDIESEL-45-CL-2038940`, reported version `1.0.3 CL 2038940`),
  and activation of the Bloody Harvest event
  ([Day-of GBX Post](https://borderlands.com/en-US/news/2019-10-24-borderlands-3-patch-hotfixes-roadmap-oct-24/),
  [Local Post Archive](gbx_info_archive/2019-10-24-patch_and_hotfixes.md),
  [Event Details GBX Post](https://borderlands.com/en-US/news/2019-10-21-bloody-harvest-trailer-info/),
  [Local Post Archive](gbx_info_archive/2019-10-21-bloody_harvest_trailer.md))
  * A very small second hotfix update was applied a few hours later, related to
    Twitch chest interactions (just one additional hotfix)
* **2019-10-25**: Small hotfix update to tweak Captain Haunt slightly (increased
  volume and better loot drops)
  ([GBX Tweet](https://twitter.com/GearboxOfficial/status/1187898114935590913),
  [Local Archive](gbx_info_archive/2019-10-25-captain_haunt_tweak.md))
* **2019-10-29**: Week 4 hotfixes were partially removed (namely Twitch
  interaction and Mayhem XP buffs).  The rest of Week 4 is being left in as
  permanent changes.
* **2019-10-31**: Seventh announced hotfixes.
  ([GBX Post](https://borderlands.com/en-US/news/2019-10-31-borderlands-3-hotfixes-oct-31/),
  [Local Post Archive](gbx_info_archive/2019-10-31-hotfixes.md))
* **2019-11-01**: Halloween-specific hotfix to have 100% haunted enemies was
  removed.
* **2019-11-07**: Eighth announced hotfixes.
  ([GBX Post](https://borderlands.com/en-US/news/2019-11-07-borderlands-3-hotfixes-nov-7/),
  [Local Post Archive](gbx_info_archive/2019-11-07-hotfixes.md))
* **2019-11-14**: Ninth announced hotfixes.
  ([GBX Post](https://borderlands.com/en-US/news/2019-11-14-borderlands-3-hotfixes-nov-14),
  [Local Post Archive](gbx_info_archive/2019-11-14-hotfixes.md))
  * An unannounced update a few hours after that got rid of a couple of
    hotfixes.
* **2019-11-21**: Tenth announced hotfixes, fourth official patch (build
  version `OAK-PATCHDIESEL-71-CL2060134`, reported version `1.0.4 CL 2060134`),
  and release of Takedown at Maliwan's Blacksite, and introduction of
  Mayhem 4.  Nearly half of the previously-established hotfixes have been
  removed, presumably because they're now baked into the game data.  A few
  hours later, some newer hotfixes were added to the mix.
  ([GBX Post](https://borderlands.com/en-US/news/2019-11-21-borderlands-3-patch-hotfixes-nov-21/),
  [Local Post Archive](gbx_info_archive/2019-11-21-patch_and_hotfixes.md))
* **2019-11-22**: Small hotfix update to revert a change to Megavore which was
  having unintended consequences.  Also seems to add in some sniper rifle buffs
  which had been removed with yesterday's update.
  ([GBX Tweet](https://twitter.com/GearboxOfficial/status/1198014507991224320),
  [Local Archive](gbx_info_archive/2019-11-22-megavore_revert.md))
* **2019-11-26**: Eleventh announced hotfixes, just a quick fix to the Butcher.
  ([GBX Post](https://borderlands.com/en-US/news/2019-11-26-borderlands-3-hotfixes-nov-26/),
  [Local Archive](gbx_info_archive/2019-11-26-hotfixes.md))
* **2019-12-05**: Twelfth announced hotfixes, including disabling the Bloody
  Harvest event.
  ([GBX Post](https://borderlands.com/en-US/news/2019-12-05-borderlands-3-hotfixes-dec-5/),
  [Local Archive](gbx_info_archive/2019-12-05-hotfixes.md))
* **2019-12-10**: Unannounced patch to the game EXE, it seems (build version
  seems to have remained `OAK-PATCHDIESEL-71-CL2060134`, but the reported
  version is now `1.0.4 CL 2060135`)
* **2019-12-12**: Fifth official patch (build version `OAK-PATCHDIESEL-97-CL2077505`,
  reported version `1.0.5 CL 2077505`), fixing various bugs in the engine and laying
  the groundwork for the upcoming Moxxi Heist DLC.  Also includes the welcome change
  of having a main-menu notification for when hotfixes are loaded!
  ([GBX Post](https://borderlands.com/en-US/news/2019-12-12-borderlands-3-patch-dec-12/),
  [Local Archive](gbx_info_archive/2019-12-12-patch.md))
  Additionally, there were three smallish hotfix updates throughout the day, which
  were mostly just minor cleanup stuff, though the last of them buffed the droprates
  of rare spawns, trial bosses, and slaughter bosses.
  ([GBX Tweet](https://twitter.com/Borderlands/status/1205217625959096320),
  [Local Archive](gbx_info_archive/2019-12-12-tweet.md))
* **2019-12-13**: Small hotfix update which tweaks the R4kk P4ck COM, and fixes
  Zane's barrier in a couple of situations.
  ([GBX Tweet](https://twitter.com/Borderlands/status/1205669994807250944),
  [Local Archive](gbx_info_archive/2019-12-13-tweet.md))
* **2019-12-19**: Release of DLC1 (Moxxi's Heist of the Handsome Jackpot), minor
  patch (build version `OAK-PATCHDIESEL-99-CL2079527`, reported version `1.0.5 CL 2079527`),
  and the thirteenth announced hotfix updates.
  ([GBX Post](https://borderlands.com/en-US/news/2019-12-19-borderlands-3-hotfixes-dec-19/),
  [Local Archive](gbx_info_archive/2019-12-19-hotfixes_and_dlc1.md))
* **2020-01-02**: Hotfixes updated to remove Christmas-themed main menu.
* **2020-01-09**: Fourteenth announced hotfixes, just tweaking a few minor things.
  ([GBX Post](https://borderlands.com/en-US/news/2020-01-09-borderlands-3-hotfixes-jan-9/),
  [Local Archive](gbx_info_archive/2020-01-09-hotfixes.md))
* **2020-01-16**: Fifteenth announced hotfixes, including the Farming Frenzy
  event and temporary scaling changes to the Maliwan Takedown.  A minor
  hotfix update later in the day cleaned up some duplicate statements.
  ([GBX Post](https://borderlands.com/en-US/news/2020-01-16-borderlands-3-hotfixes-jan-16/),
  [Local Archive](gbx_info_archive/2020-01-16-hotfixes.md) -
  [Farming Frenzy Post](https://borderlands.com/en-US/news/2020-01-15-borderlands-3-farming-frenzy/),
  [Local Archive](gbx_info_archive/2020-01-15-farming_frenzy.md))
* **2020-01-17**: A small hotfix update to tweak Urist Enforcer's drop rate
  a bit, though earlier hotfixes still in the file might mean the buff isn't
  applying.  Also the tweet from GBX implies that it was supposed to have
  buffed a bunch of other enemy drops as well, which it doesn't actually do.
  ([GBX Tweet](https://twitter.com/GearboxOfficial/status/1218233115296124936),
  [Local Archive](gbx_info_archive/2020-01-17-tweet.md))
* **2020-01-23**: Sixteenth announced hofixes, just various bugfixes and
  balance changes.
  ([GBX Post](https://borderlands.com/en-US/news/2020-01-23-borderlands-3-hotfixes-jan-23/),
  [Local Archive](gbx_info_archive/2020-01-23-hotfixes.md))
* **2020-01-30**: Seventeenth announced hotfixes, and introduction of Rare Chest
  Riches event.  Farming Frenzy event will apparently remain active permanently.
  ([GBX Post](https://borderlands.com/en-US/news/2020-01-30-borderlands-3-hotfixes-jan-30/),
  [Local Archive](gbx_info_archive/2020-01-30-rare_chest_riches.md))
* **2020-02-04**: A small unannounced hotfix update which tweaks Cistern of
  Slaughter, presumably just bugfixes.
* **2020-02-05**: Another small unannounced hotfix which nerfs some of the 40% drop rates
  introduced in the Farming Frenzy event down to 30%.
* **2020-02-13**: Sixth official patch (build version `OAK-PATCHDIESEL0-45-CL2109921`,
  reported version `1.0.6 CL 2109921`), eighteenth announced hotfixes, and introduction of
  Broken Hearts timed content update.  Level cap increase to 53, among other changes.
  ([GBX Post](https://borderlands.com/en-US/news/2020-02-13-borderlands-3-patch-hotfixes-feb-13/),
  [Local Archive](gbx_info_archive/2020-02-13-patch_hotfixes_broken_hearts.md))
  * A small hotfix update a few hours later disabled the Rare Chest Riches event.
* **2020-02-20**: Nineteenth announced hotfixes, and deactivation of Broken Hearts
  event.
  ([GBX Post](https://borderlands.com/en-US/news/2020-02-20-borderlands-3-hotfixes-feb-20/),
  [Local Archive](gbx_info_archive/2020-02-20-hotfixes.md))
  * A small hotfix update afterwards removed a few Broken Hearts-specific balance changes
    which were missed on the initial update.
* **2020-02-27**: Twentieth announced hotfixes - various bugfixes and weapon buffs.
  ([GBX Post](https://borderlands.com/en-US/news/2020-02-27-borderlands-3-hotfixes-feb-27/),
  [Local Archive](gbx_info_archive/2020-02-27-hotfixes.md))
  * A small update a little while later added one more buff to the Lob.
* **2020-03-05**: 21st announced hotfixes - various weapon buffs, mostly.  A small update
  prior to the official update also changed the hotfix service identifier to be cross-play
  compatible, presumably in preparation for the BL3 Steam release.
  ([GBX Post](https://borderlands.com/en-US/news/2020-03-05-borderlands-3-hotfixes-mar-5/),
  [Local Archive](gbx_info_archive/2020-03-05-hotfixes.md))
* **2020-03-12**: 22nd announced hotfixes - various announced changes, though the only ones
  which are actually active in today's hotfix are weapon buffs.  The rest will apparently
  be rolled out over the next day.
  ([GBX Post](https://borderlands.com/en-US/news/2020-03-12-borderlands-3-hotfixes-mar-12/),
  [Local Archive](gbx_info_archive/2020-03-12-hotfixes.md))
* **2020-03-13**: A couple more hotfix updates throughout the day completed the implementation
  of the announced hotfix updates from the previous day.  Also the first release on Steam
  (version `OAK-PATCHWIN64-49-CL2141850`), and a patch to the EGS version, to finish up
  cross-play between EGS and Steam, with a few other minor tweaks (build version
  `OAK-PATCHDIESEL2-32-CL2141850`, reported version `1.0.6 CL 2141850`)
  ([GBX Post](https://borderlands.com/en-US/news/2020-03-12-borderlands-3-epic-patch-mar-13/),
  [Local Archive](gbx_info_archive/2020-03-13-patch_xplay.md))
* **2020-03-19**: 23rd announced hotfixes - just some various tweaks here and there.
  ([GBX Post](https://borderlands.com/en-US/news/2020-03-19-borderlands-3-hotfixes-mar-19/),
  [Local Archive](gbx_info_archive/2020-03-19-hotfixes.md))
* **2020-03-24**: Start of "Takedown Shakedown" event which guarantees drops from Wotan and
  Valkyrie Squad, and increases the number of drops from each.
  ([GBX Post](https://borderlands.com/en-US/news/2020-03-24-takedown-shakedown/),
  [Local Archive](gbx_info_archive/2020-03-24-takedown_shakedown.md))
* **2020-03-26**: Release of DLC2 (Hibiscus - Guns, Love, and Tentacles), seventh announced
  patch (EGS build version `OAK-PATCHDIESEL1-102-CL2149333`, EGS reported version
  `1.0.7_CL_2149333_Borderlands_3`, Steam build version `OAK-PATCHWIN641-32-CL2149333`),
  level cap increase to 57, and 24th announced hotfixes.
  ([GBX Post](https://borderlands.com/en-US/news/2020-03-26-borderlands-3-patch-hotfixes-mar-26/),
  [Local Archive](gbx_info_archive/2020-03-26-hotfixes_and_dlc2.md))
  * DLC2 rolled out in stages for Epic -- a pre-patch first, then the DLC
    itself.  Steam users got the pre-patch and DLC all in one go.
  * A few smaller hotfix updates trickled in throughout the day:
    * The first re-added some Lob buffs which were taken out incorrectly
    * The next rearranged those in the hotfix list
    * The next re-added in a bunch of other hotfixes which had been taken out incorrectly
* **2020-03-27**: "Door Busters" mini event, which guarantees legendary items in
  vending machines.  Will run through April 2.
  ([GBX Tweet](https://twitter.com/Borderlands/status/1243588733061890048),
  [Local Archive](gbx_info_archive/2020-03-27-door_busters_mini_event.md))
  * Another hotfix later in the day added the "Co-op Loot Drop" event, running concurrently
    with "Door Busters."  This one's only active through the weekend.
    ([GBX Post](https://borderlands.com/en-US/news/2020-03-27-co-op-loot-drop/),
    [Local Archive](gbx_info_archive/2020-03-27-co-op_loot_drop.md))
* **2020-04-01**: April Fool's surprise update which makes characters, pets, and clones
  tiny.
* **2020-04-02**: 25th announced hotfixes, with various balance tweaks.  Removal of April
  Fool's updates, Takedown Shakedown, Door Busters event, and Co-op Loot Drop event.
  Addition of Slot Machine Mania and Trials Take-All events.
  ([GBX Post](https://borderlands.com/en-US/news/2020-04-02-borderlands-3-hotfixes-apr-2/),
  [Local Archive](gbx_info_archive/2020-04-02-slot_machine_mania_and_trials_take-all.md))
  * One of the hotfix values was tweaked a bit later in the day, as well.
* **2020-04-03**: Tweak to the R4kk P4k COM, to address some crashes.
  ([GBX Post](https://forums.gearboxsoftware.com/t/borderlands-3-hotfix-04-02-20/4463884),
  [Local Archive](gbx_info_archive/2020-04-03-r4kk_p4k_fix.md))
* **2020-04-07**: Activation of Citizen Science event.
  ([GBX Post](https://borderlands.com/en-US/news/2020-04-07-borderlands-science/),
  [Local Archive](gbx_info_archive/2020-04-07-citizen_science.md))
* **2020-04-09**: 26th announced hotfixes, with various buffs to Moze.  Also added Rare
  Chest Riches and Loot Monster Mayhem events, and removed Slot Machine Mania and Trials
  Take-All events.
  ([GBX Post](https://borderlands.com/en-US/news/2020-04-09-borderlands-3-hotfixes-apr-9/),
  [Local Archive](gbx_info_archive/2020-04-09-rare_chest_riches_and_loot_monster_mayhem.md))
* **2020-04-16**: 27th announced hotfixes.  Introduction of Slaughter Onslaught and
  Making It Rain events, and removal of Rare Chest Riches and Loot Monster Mayhem.
  ([GBX Post](https://borderlands.com/en-US/news/2020-04-16-borderlands-3-hotfixes-apr-16/),
  [Local Archive](gbx_info_archive/2020-04-16-slaughter_onslaught_and_making_it_rain.md))
* **2020-04-23**: Eighth announced patch (EGS build version `OAK-PATCHDIESEL-178-CL2173119`,
  EGS reported version `1.0.8_CL_2173119_Borderlands_3`, Steam build version
  `OAK-PATCHWIN64-79-CL2173119`), and 28th announced hotfixes.
  Introduction of Mayhem 2.0, which replaces the old Mayhem Mode, and start of Revenge of
  the Cartels event.  Also the start of the first Loot the Universe mini-event, on Pandora.
  Disabling of Slaughter Onslaught and Making It Rain events.
  ([GBX Post](https://borderlands.com/en-US/news/2020-04-23-borderlands-3-patch-hotfixes-apr-23/),
  [Local Archive](gbx_info_archive/2020-04-23-patch_mayhem2_and_cartels.md))
* **2020-04-24**: Small update to disable the Boundary Issues Mayhem 2.0 modifier,
  which was causing audio problems.
  ([GBX Tweet](https://twitter.com/Borderlands/status/1253788264743358464),
  [Local Archive](gbx_info_archive/2020-04-24-tweet.md))
* **2020-04-27**: Small update to disable the Drone Ranger Mayhem 2.0 modifier,
  which was causing audio problems.
  ([GBX Tweet](https://twitter.com/Borderlands/status/1254831343457808385),
  [Local Archive](gbx_info_archive/2020-04-27-tweet.md))
* **2020-04-30**: 29th announced hotfixes.  Disabling of Co-Op Loot Drop event, and
  the Loot the Universe mini-event moves from Pandora to Promethea (and Athenas).
  Various bugfixes and tweaks, as well.
  ([GBX Post](https://borderlands.com/en-US/news/2020-04-30-borderlands-3-hotfixes-apr-30/),
  [Local Archive](gbx_info_archive/2020-04-30-loot_the_universe_promethea.md))
  * A small update later in the day fixed Anointment droprates for shields,
    when in Mayhem modes.
    ([GBX Tweet](https://twitter.com/GearboxOfficial/status/1255999366680248320),
    [Local Archive](gbx_info_archive/2020-04-30-tweet.md))
* **2020-05-07**: 30th announced hotfixes.  Moving Loot the Universe mini-event
  from Promethea/Athenas to Eden-6, and a few Mayhem 2.0 drop fixes.
  ([GBX Post](https://borderlands.com/en-US/news/2020-05-07-borderlands-3-hotfixes-may-7/),
  [Local Archive](gbx_info_archive/2020-05-07-loot_the_universe_eden6.md))
* **2020-05-14**: 31st announced hotfixes.  Moving Loot the Universe mini-event
  from Eden-6 to Nekrotafeyo/Trials.  Also a few bugfixes and loot drop changes.
  ([GBX Post](https://borderlands.com/en-US/news/2020-05-14-borderlands-3-hotfixes-may-14/),
  [Local Archive](gbx_info_archive/2020-05-14-loot_the_universe_nekrotafeyo.md))
* **2020-05-21**: 32nd announced hotfixes.  Loot the Universe Mini-Event is over,
  plus a couple of bugfixes.
  ([GBX Post](https://borderlands.com/en-US/news/2020-05-21-borderlands-3-hotfixes-may-21/),
  [Local Archive](gbx_info_archive/2020-05-21-hotfixes.md))
* **2020-05-28**: 33rd announced hotfixes.  Just a single bugfix.
  ([GBX Post](https://borderlands.com/en-US/news/2020-05-28-borderlands-3-hotfixes-may-28/),
  [Local Archive](gbx_info_archive/2020-05-28-hotfixes.md))
* **2020-06-11**: Ninth announced patch (EGS build version `OAK-PATCHDIESEL1-137-CL2205777`,
  EGS reported version `1.0.9_Borderlands_3`, Steam build version
  `OAK-PATCHWIN641-63-CL2205777`), and 28th announced hotfixes.
  Addition of Guardian Takedown event, and closure of Revenge of the Cartels.  Lots of various
  bugfixes and tweaks, as well.
  ([GBX Post](https://borderlands.com/en-US/news/2020-06-11-borderlands-3-patch-hotfixes-june-11/),
  [Local Archive](gbx_info_archive/2020-06-11-guardian_takedown.md))
* **2020-06-16**: Small hotfix to nerf the Guardian Takedown health values, to about half
  of their previous values.
  ([GBX Tweet](https://twitter.com/GearboxOfficial/status/1272985801341747201),
  [Local Archive](gbx_info_archive/2020-06-16-tweet_-_guardian_takedown_nerf.md))
* **2020-06-18**: 34th announced hotfixes, buffing up the Web Slinger, and fixing some
  grammatical errors.
  ([GBX Post](https://borderlands.com/en-US/news/2020-06-18-borderlands-3-hotfixes-june-18/),
  [Local Archive](gbx_info_archive/2020-06-18-hotfixes.md))
* **2020-06-25**: 10th announced patch (EGS build version `OAK-PATCHDIESEL0-103-CL2234726`,
  EGS reported version `1.0.10_CL_2234726_Borderlands_3`, Steam build version
  `OAK-PATCHWIN640-59-CL2234726`), 35th announced hotfixes, release of DLC3 (Bounty of
  Blood), Mayhem 2.0 Tweaks Phase 2, and level cap increase to 60.  The patch and the
  rollout of DLC3 were probably separated by a bit of time, but they happened within
  an hour or two of each other.
  ([GBX Post](https://borderlands.com/en-US/news/2020-06-25-borderlands-3-patch-hotfixes-june-25/),
  [Local Archive](gbx_info_archive/2020-06-25-hotfixes_and_dlc3.md))
  * A separate hotfix a little while later fixed some issues with Zane's Digi-Clones and Moze's
    Iron Bear.
* **2020-06-26**: Two small unannounced hotfix updates made some balance tweaks
  to a few Operative and Gunner skills.
* **2020-07-02**: 36th announced hotfixes, re-enabling the two previously-disabled Mayhem 2.0
  Modifiers (Boundary Issues and Drone Ranger), along with a few other bugfixes.
  ([GBX Post](https://borderlands.com/en-US/news/2020-07-02-borderlands-3-hotfixes-july-2/),
  [Local Archive](gbx_info_archive/2020-07-02-hotfixes.md))
* **2020-07-09**: 37th announced hotfixes, mostly just some bugfixes for Lucky 7.
  ([GBX Post](https://borderlands.com/en-US/news/2020-07-09-borderlands-3-hotfixes-july-9/),
  [Local Archive](gbx_info_archive/2020-07-09-hotfixes.md))
* **2020-07-23**: 11th announced patch (EGS build version `OAK-PATCHDIESEL-222-CL2256815`,
  EGS reported version `1.0.11_CL_2256815_Borderlands_3`, Steam build version
  `OAK-PATCHWIN64-123-CL2256815`), and 38th announced hotfixes.  Various tweaks
  and bugfixes all around, and a redistribution of unique drops (which also enabled
  respawning of a number of named enemies who would previously only spawn once per playthough).
  ([GBX Post](https://borderlands.com/en-US/news/2020-07-23-borderlands-3-patch-hotfixes-july-23/),
  [Local Archive](gbx_info_archive/2020-07-23-patch_and_hotfixes.md))
  * A second, smaller hotfix update happened an hour or two later, to disable
    the various anointments they'd mentioned in the initial update.
* **2020-07-30**: 39th announced hotfixes, and start of the first BL3 Anniversary Celebration
  event: ECHOcast Overload.
  ([GBX Post](https://borderlands.com/en-US/news/2020-07-30-borderlands-3-hotfixes-july-30/),
  [Local Archive](gbx_info_archive/2020-07-30-anniversary_1_echocast_overload.md))
  * A second small hotfix update an hour or so later contained one fix to a red chest, in
    relation to the event.
* **2020-08-06**: 40th announced hotfixes, end of the "ECHOcast Overload" event, and start
  of the Bonus Boss Loot event.
  ([GBX Post](https://borderlands.com/en-US/news/2020-08-06-borderlands-3-hotfixes-aug-6/),
  [Local Archive](gbx_info_archive/2020-08-06-anniversary_2_bonus_boss_loot.md))
  * A second minor hotfix update added in the Beastmaster fix listed there.
  * A third update later in the day added in some missed bosses for the event.
* **2020-08-13**: 41st announced hotfixes, end of the Bonus Boss Loot event, and start of
  the Loot Monster Mayhem event.
  ([GBX Post](https://borderlands.com/en-US/news/2020-08-13-borderlands-3-hotfixes-aug-13/),
  [Local Archive](gbx_info_archive/2020-08-13-anniversary_3_loot_monster_mayhem.md))
  * A second hotfix update a few hours later *actually* removed the Bonus
    Boss Loot event; for awhile the two events were running at the same time.
  * A third small update temporarily disabled the Chain Gang mayhem modifier for the
    duration of the event.
    ([GBX Tweet](https://twitter.com/Borderlands/status/1294056405624737792),
    [Local Archive](gbx_info_archive/2020-08-13-tweet_-_chain_gang_temp_disable.md))
* **2020-08-20**: 42nd announced hotfixes, end of the Loot Monster Mayhem event, and
  start of the Show Me The Eridium event.  Also a tweak to Guardian Takedown drops,
  buffs to some specific gear, and a few NPC tweaks from DLC3.
  ([GBX Post](https://borderlands.com/en-US/news/2020-08-20-borderlands-3-hotfixes-aug-20/),
  [Local Archive](gbx_info_archive/2020-08-20-anniversary_4_show_me_the_eridium.md))
* **2020-08-21**: Various weapon-buff hotfixes were updated to "Early Level" hotfixes, which
  apparently makes the buffs survive quits to the main menu a bit better.
  ([GBX Tweet](https://twitter.com/Borderlands/status/1296954688105877504),
  [Local Archive](gbx_info_archive/2020-08-21-tweet.md))
* **2020-08-27**: 43rd announced hotfixes, end of the Show Me The Eridium event, and
  start of the Mayhem Made Mild Event.
  ([GBX Post](https://borderlands.com/en-US/news/2020-08-27-borderlands-3-hotfixes-aug-27/),
  [Local Archive](gbx_info_archive/2020-08-27-anniversary_5_mayhem_made_mild.md))
* **2020-09-03**: 44th announced hotfixes, end of the Mayhem Made Mild event, and
  start of the Making It Rain event.  Also a few weapon buffs and drop rate adjustments.
  ([GBX Post](https://borderlands.com/en-US/news/2020-09-03-borderlands-3-hotfixes-sept-3/),
  [Local Archive](gbx_info_archive/2020-09-03-anniversary_6_making_it_rain.md))
  * A minor update a few hours later tweaked the Hellwalker buff to survive
    main-menu reloads.
* **2020-09-10**: Release of DLC4 (Psycho Krieg and the Fantastic Fustercluck), 45th announced 
  hotfixes, and 12th announced patch (EGS build version `OAK-PATCHDIESEL1-191-CL2267649`,
  EGS reported version `1.0.12_CL_2267649_Borderlands_3`, Steam build version
  `OAK-PATCHWIN641-118-CL2267649`).
  ([GBX Post](https://borderlands.com/en-US/news/2020-09-10-borderlands-3-patch-hotfixes-sept-10/),
  [Local Archive](gbx_info_archive/2020-09-10-hotfixes_and_dlc4.md))
  * A minor hotfix update shortly after release disabled the Making It Rain anniversary
    event.
  * Another update a few hours later added in some bugfixes for some issues that were
    affecting players in the new DLC.
* **2020-09-11**: Minor unannounced hotifx with a couple more bugfixes for DLC4
* **2020-09-17**: 46th announced hotfixes, just some fixes to spawns in Guardian Takedown.
  Announcement that hotfix release cadence will be slowing down in the future, so expect
  fewer of these updates!
  ([GBX Post](https://borderlands.com/en-US/news/2020-09-17-borderlands-3-hotfixes-sept-17/),
  [Local Archive](gbx_info_archive/2020-09-17-hotfixes.md))
* **2020-10-08**: 47th announced hotfixes, and the re-launch of Bloody Harvest event for
  2020.  Also includes several tweaks to Haunted anointments, buffs to gear, buffs to
  various Operative skills and COMs, and some general bugfixes.
  ([GBX Post](https://borderlands.com/en-US/news/2020-10-08-borderlands-3-hotfixes-oct-8/),
  [Local Archive](gbx_info_archive/2020-10-08-bloody_harvest_2020.md))
  * The first hotfix actually just contained the tweaks, buffs, and bugfixes.  A second
    hotfix update a little after *actually* enabled the Bloody Harvest event again.
* **2020-10-15**: 48th announced hotfixes, bringing some tweaks to Bloody
  Harvest, some bugfixes, and some buffs for various weapons and grenades.
  ([GBX Post](https://borderlands.com/en-US/news/2020-10-15-borderlands-3-hotfixes-oct-15/),
  [Local Archive](gbx_info_archive/2020-10-15-hotfixes.md))
  * A couple of updates throughout the day fixed a few issues with the
    original batch of hotfixes, too.
* **2020-11-05**: Disabled the Bloody Harvest 2020 event.
* **2020-11-09**: Release of the Designer's Cut DLC (fourth Skill Trees, Arms Race),
  13th announced patch (EGS build version `OAK-PATCHDIESEL0-200-CL2297688`,
  EGS reported version `1.0.13_CL_2297688_Borderlands_3`, Steam build version
  `OAK-PATCHWIN640-149-CL2297688`), Mayhem 11, level cap increase to 65, and 49th announced
  hotfixes.
  ([GBX Post](https://borderlands.com/en-US/news/2020-11-09-borderlands-3-patch-hotfixes-nov-9/),
  [Local Archive](gbx_info_archive/2020-11-09-designers_cut.md))
  * A small hotfix tweak was released a few hours later which removed a couple of
    hotfixes.
  * A second, unannounced patch (and data update) was released about twelve hours
    afterwards, presumably containing various bugfixes.  (EGS build version
    `OAK-PATCHDIESEL-226-CL2318486`, EGS reported version `1.0.14_CL_2318486_Borderlands3`,
    Steam build version `OAK-PATCHWIN64-127-CL2318486`)
* **2020-11-19**: 50th announced hotfixes, with a couple bugfixes and activation of the
  "Golden Path" event.
  ([GBX Post](https://borderlands.com/en-US/news/2020-11-19-borderlands-3-hotfixes-nov-19/),
  [Local Archive](gbx_info_archive/2020-11-19-golden_path.md))
* **2020-12-03**: Golden Path event was deactivated (no official announcement of such, though
  this was the scheduled end date for it).
* **2020-12-17**: 51st announced hotfixes, enabling a new Co-op Loot Drop Event,
  buffing a bunch of weapons, and a few bugfixes.
  ([GBX Post](https://borderlands.com/en-US/news/2020-12-17-borderlands-3-hotfixes-dec-17/),
  [Local Archive](gbx_info_archive/2020-12-17-co-op_loot_drop.md))
* **2020-12-31**: A small unannounced hotfix change turned off the holiday-themed main menu.
* **2021-01-14**: 52nd announced hotfixes, enabling a new Supercharged Crystals event,
  along with some gear buffs.
  ([GBX Post](https://borderlands.com/en-US/news/2021-01-14-borderlands-3-hotfixes-jan-14/),
  [Local Archive](gbx_info_archive/2021-01-14-supercharged_crystals.md))
* **2021-01-21**: 14th announced patch (EGS build version `OAK-PATCHDIESEL0-224-CL2341468`,
  EGS reported version `1.0.15_CL_2341468_Borderlands_3`, Steam build version
  `OAK-PATCHWIN640-172-CL2341468`), 53rd announced hotfixes, end of Supercharged Crystals
  event, and start of Clear Skies event.  A few more gear buffs, as well.
  ([GBX Post](https://borderlands.com/en-US/news/2021-01-21-borderlands-3-update-hotfixes-jan-21/),
  [Local Archive](gbx_info_archive/2021-01-21-clear_skies.md))
* **2021-01-22**: A small hotfix update was pushed to fix some Iron Cub
  scaling issues.
  ([GBX Tweet](https://twitter.com/Borderlands/status/1352664415724662787),
  [Local Archive](gbx_info_archive/2021-01-22-tweet.md))
  * An unannounced hotfix update a few hours later removed an older hotfix
    relating to Guardian Takedown pads, probably remnants of the Supercharged
    Crystals event.
* **2021-01-28**: 54th announced hotfixes, end of the Clear Skies event, and start of the
  Extra Extra Extraction event.
  ([GBX Post](https://borderlands.com/en-US/news/2021-01-28-borderlands-3-hotfixes-jan-28/),
  [Local Archive](gbx_info_archive/2021-01-28-extra_extra_extraction.md))
* **2021-02-04**: 55th announced hotfixes, end of the Extra Extra Extraction event,
  and s4tart of the Gear Rush event.
  ([GBX Post](https://borderlands.com/en-US/news/2021-02-04-borderlands-3-hotfixes-feb-4/),
  [Local Archive](gbx_info_archive/2021-02-04-gear_rush.md))
* **2021-02-11**: 56th announced hotfixes, and beginning of
  Broken Hearts 2021.  Also some more gear buffs.
  ([GBX Post](https://borderlands.com/en-US/news/2021-02-11-borderlands-3-hotfixes-feb-11/),
  [Local Archive](gbx_info_archive/2021-02-11-broken_hearts.md))
  * A small update a little while after correctly added in the Kaoson buff,
    which was omitted from the original hotfix update.
  * A third update happened later in the day which only changed an internal
    version number -- no actual hotfix changes were present in the third
    update today.
* **2021-02-18**: Unannounced hotfix update which disabled the Gear Rush
  event (which was originally supposed to have been disabled last week).
* **2021-02-23**: Tweaked the Broken Hearts event slightly to remove the level
  restriction on Polyaimorous and Wedding Invitation, and make those items
  droppable from hearts, rather than just as heart-killing rewards.
  ([GBX Tweet](https://twitter.com/Borderlands/status/1364291664500588549),
  [Local Archive](gbx_info_archive/2021-02-23-broken_hearts_tweak_tweet.md))
* **2021-02-25**: End of the Broken Hearts event -- no other hotfix updates.
* **2021-03-11**: 57th announced hotfixes, with some more gear buffs,
  nerfs to the Siren's Remnant skill, and adding loot sources for R.Y.N.A.H.
  and Firestorm grenade mod.
  ([GBX Post](https://borderlands.com/en-US/news/2021-03-11-borderlands-3-hotfixes-mar-11/),
  [Local Archive](gbx_info_archive/2021-03-11-hotfixes.md))
* **2021-04-01**: 58th announced hotfixes: re-launch of Show Me The Eridium
  event, some character balancing, weapon buffs, and other smaller fixes.  Also
  a reprise of last year's April Fools joke, which makes all characters, pets, and
  clones tiny.
  ([GBX Post](https://borderlands.com/en-US/news/2021-04-01-borderlands-3-hotfixes-apr-1/),
  [Local Archive](gbx_info_archive/2021-04-01-show_me_the_eridium.md))
  * A small update an hour or two later fixed an issue with their Try-Bolt buff
* **2021-04-02**: Removal of the April Fool's joke from yesterday.
* **2021-04-08**: 15th announced patch (Steam build version
  `OAK-PATCHWIN641-227-CL2425795`, EGS versions forthcoming), 59th announced
  hotfixes, launch of DLC6 (Director's Cut) and all its associated additions
  to the game.
  ([GBX Post](https://borderlands.com/en-US/news/2021-04-08-borderlands-3-update-hotfixes-apr-8/),
  [Local Archive](gbx_info_archive/2021-04-08-directors_cut.md))
  * Two unannounced hotfix updates happened during the day after the patch
    was released, presumably fixing some bugs.
* **2021-04-15**: 60th announced hotfixes, with various bugfixes and some
  drop rate tweaks.
  ([GBX Post](https://borderlands.com/en-US/news/2021-04-15-borderlands-3-hotfixes-apr-15/),
  [Local Archive](gbx_info_archive/2021-04-15-hotfixes.md))
* **2021-04-22**: 61st announced hotfixes, with tweaks to drop rates,
  addition of some DLC3 drop sources, and increased eridium rewards from
  various sources.
  ([GBX Post](https://borderlands.com/en-US/news/2021-04-22-borderlands-3-hotfixes-apr-22/),
  [Local Archive](gbx_info_archive/2021-04-22-hotfixes.md))
  * Another update a few hours later removed some old Trials-chest hotfixes
    which were no longer appropriate with today's updates.
* **2021-04-29**: 62nd announced hotfixes, mostly with some gear buffs.
  ([GBX Post](https://borderlands.com/en-US/news/2021-04-29-borderlands-3-hotfixes-apr-29/),
  [Local Archive](gbx_info_archive/2021-04-29-hotfixes.md))
* **2021-04-30**: A small unannounced hotfix update removed some old gear
  balance hotfixes which were obsoleted by yesterday's update.
  * A second update an hour or so later did a little more of the same.

