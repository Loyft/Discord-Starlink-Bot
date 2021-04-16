# Discord-Starlink-Bot
Discord Bot that fetches news related to space

![Starlink Bot Profile Picture](images/github_starlink.png?raw=true "Title")

#### Commands

*prefix: _*

Command | Response
------- | --------
_info   | Shows info about Starlink Bot
_iss    | Gets the current location of the ISS
_inv    | Shows invite link for Starlink Bot

#### News

Starlink Bot automatically gets new top posts from the subreddits: r/space, r/spacex, and r/nasa and posts them into the corresponding channels.

#### Changelog
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
