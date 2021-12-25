# Deploy with github worklows
**Required:**
1. Github account
2. Heroku Account
3. Time and coffee😜


## STEP TO DEPLOY:
<details>
   <summary><b>Click for more Tutorial details</b></summary>

1. Fork a repo

![Fork](https://telegra.ph/file/aa95e3040cf71276281bc.jpg)

2. Go to your fork repo settings » secrets. tap New Repository Secret to fill out the variable.

![secrets](https://telegra.ph/file/dd7475fc5e875f833bdae.jpg)

3. Fill The require variable
   - ```HEROKU_EMAIL``` : You heroku email which deployed as userbot
   - ```HEROKU_API_KEY``` : Your heroku api, get from [Here](https://dashboard.heroku.com/account). Scroll down, you will get it.
   - ```HEROKU_APP_NAME``` : Fill by unique name, must be lowercase letters, numbers, and dashes.
   
![example](https://telegra.ph/file/bcbde93c0757e3711467e.jpg)

   - ```CONFIG_FILE_URL``` : Your config.env file direct link, use secret gist for it. Copy [THIS](https://github.com/gudmeong/UserButt/blob/sql-extended/config.env_sample), and paste to any text editor. Remove the 2st line and for many information for fill a value Read the text inside there. 
   - if you already done fill out a variable and value inside there. Copy All Text and open https://gist.github.com paste in there and give a name file as ```config.env```, create a secret gist.

![gist](https://telegra.ph/file/f3d5788509a065d770fb6.jpg)

4. Notice Important
   - After create it, tap raw button then copy a raw link

![Raw](https://telegra.ph/file/942efafa7bb7b26990ba5.jpg)

![Raw2](https://telegra.ph/file/3326a9570cd57fbe551d2.jpg)

   - Paste raw gist link to ```CONFIG_FILE_URL```, Remove commit id from a raw link
   - Before: ```https://gist.githubusercontent.com/gudmeong/3346b1f800b88106f717cc417eb34688/raw/a244e7c2e9592f9503a2566353e2b6af9d2929d1/config.env```
   - After: ```https://gist.githubusercontent.com/gudmeong/3346b1f800b88106f717cc417eb34688/raw/config.env```
   

5. After adding Require value in github repo secrets, Go to tab actions in your fork repository.
   - Select Heroku Container as show bellow:
  
![heroku container](https://telegra.ph/file/d983f60106d5819a93591.jpg)

6. Click on Run workflow and select sql-extended branch, then run a workflow

![Run](https://telegra.ph/file/d2082c9f708d554c88751.jpg)

After deploy is finished without error, check your heroku app then switch dyno to on

</details>

## Setup Database
```
We are using database heroku postgress sql
```
- open your heroku app a which deploying userbot, and select like pict below

![postgressl](https://telegra.ph/file/3a7712d7bb40daa7c35e3.jpg)

- Submit then

__Now Switch you dyno worker to for run a userbot__

# Little tip
- You can change any value on CONFIG_FILE_URL (secret gist)  or by heroku vars
- If you change any value on CONFIG_FILE_URL (secret gist), you need restart for apply new value
- Or if you change or add any value by ```.set var``` or by heroku vars no need restart, because userbot do auto restarting :p
## ```Tutorial Finish```
