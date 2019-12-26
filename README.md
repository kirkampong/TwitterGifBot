# TwitterGifBot
Work in progress...
- Basic reply bot implemented using `tweepy` and `pythonanywhere`. Cloud hosted 
- Full implementation (incl. storing and vending gifs) requires more work.

Bot is live: the script lives in python anywhere : https://www.pythonanywhere.com/user/Kirkampong


## Testing the bot
* Summon the Phase1(reply) bot by mentioning @YourWiseUncle in your tweet!
* You must include #hashtag **#advice** in your tweet to get a response from the bot. This is because twitter's public APIs make it difficult to distinguish b/n replies and mentions, making it difficult to establish the expected behaviour when the tweet is not in reply to an existing tweet. 
* Media replies tested a bit. Will include this later with a new bot which will be the actual `TwitGifBot`

## Issues
* **Spurious replies** [https://github.com/kirkampong/TwitterGifBot/issues/2#issue-541421612] 
  - Twitter APIs dont deal w/replies vs mentions in a good way, making it hard to write the bot the way I want (which is slightly different from bots like `@QuotedReplies`). Was forced to add the **#advice** requirement as a (hopefully) temporary workaround. Perhaps may be possible to write a custom API just for this sometime in the future.
  
* **RateLimitError** [https://developer.twitter.com/en/docs/basics/rate-limiting] 
  - Error Msg >> `tweepy.error.RateLimitError: [{'message': 'Rate limit exceeded', 'code': 88}]`
  Twitter is now enforcing rate limits on a per-user and per-app level, which was an annoyance during testing. May not be a big problem for now since the per-app threshold is ok. However should monitor logs from time2time for RLEs.
  
