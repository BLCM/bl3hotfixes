BL3 Hotfix Archive
==================

This is an archive of the hotfixes which are being sent to Borderlands 3.
The first hotfix data was manually collected on September 21, 2019, and
the next few after that were collected manually as well.  Starting on
October 1, 2019, this project was created to check the hotfix data every
hour and write out the hotfixes automatically.

The hotfixes are written twice: once to a brand-new file which includes
a datestamp, and once to `hotfixes_current.json`.

The script which does this is written in Python 3, and should run anywhere
Python does, though you'll need to edit `output_dir` inside the script
itself to have it save out files properly.  Check `requirements.txt` inside
the script dir for the extra Python modules needed for it to run.

I've also put up a Google Sheets page which has the *all* of the hotfixes
which have been used by GBX (including ones which are no longer active)
up here: [Combined Hotfixes](https://drive.google.com/open?id=1kfkC2hJs0hZSr12bvrQlY0GyEH4S_KAI_xIAqnGmKnQ).  That sheet has all the fields split out
properly into columns, which can make hotfix investigation a lot easier.

Details
=======

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

