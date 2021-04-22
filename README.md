# Discord-Starlink-Bot
Discord Bot that fetches news related to space

![Starlink Bot Profile Picture](images/github_starlink.png?raw=true "Title")

#### Commands

*prefix: _*

Command | Response
------- | --------
_info   | Shows info about Starlink Bot
_iss    | Gets the current location of the ISS
_poll   | Creats a Poll

#### News

Starlink Bot automatically gets new top posts from reddit, collects images/videos from pr0gramm related to space, and shows current tweets from Elon Musk, posting each in their corresponding channels.

### ISS

Gets the current location of the ISS with latitude and longitude.

### Poll

Create polls with the _poll command.\
Format: "_poll question, answer1, answer2"\
Answers have to be emotes.\
\
Example: `_poll Do you want more polls? Yes or No, 👍, 👎`

![Starlink Bot Poll example](images/github_starlink_poll.png?raw=true "Title")

#### Changelog
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
