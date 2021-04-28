# Discord-Starlink-Bot
Discord Bot that fetches news related to space

![Starlink Bot Profile Picture](images/github_starlink.png?raw=true "Title")

#### Commands

*prefix: _*

Command | Response
------- | --------
_info   | Shows info about Starlink Bot
_iss    | Gets the current location of the ISS
_lvl    | Shows the current level and xp
_poll   | Creates a Poll

#### News

Starlink Bot automatically gets new top posts from reddit, collects images/videos from pr0gramm and instagram related to space, and shows current tweets from Elon Musk, posting each in their corresponding channels.

### ISS

Gets the current location of the ISS with latitude and longitude.

Command: `_iss`

![Starlink Bot ISS example](images/github_starlink_iss.png?raw=true "Title")


### Level System

Gather experience for activity on the Server. Level up and gain exclusive Roles and perks.

Command: `_lvl`

![Starlink Bot ISS example](images/github_starlink_lvl.png?raw=true "Title")

### Poll

Create polls with the _poll command.\
Format: "_poll question, answer1, answer2"\
Answers have to be emotes.\
\
Example: `_poll Do you want more polls? Yes or No, 👍, 👎`

![Starlink Bot Poll example](images/github_starlink_poll.png?raw=true "Title")

#### Changelog
- v0.5.0 - lilmayo
  - gets latest posts from lilmayo's instagram
  - #ayylmao
- v0.4.0 - Level System
  - added Level System
    - users gain experience for activity
    - automatic role assignment upon reaching different levels
    - added command `_lvl` to get current lvl and xp
  - better code structure
  - updated info section
- v0.3.1 - Cleanup
  - create polls
  - Code cleanup
- v0.3.0 - Data Collection
  - adds relevant reactions to messages
  - gets current ISS location
  - gets new tweets
  - improved handling of ids and praw
- v0.2.0 - QoL
  - gets new space related posts from pr0gramm
  - improved handling of urls, resulting in better looking posts
  - updated info section
- v0.1.0 - initial setup
  - added commands `info` and `inv`
  - added news section (spacex)
