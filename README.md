# NotionCryptoPriceUpdater

## Created by [Gareth Evens](https://www.youtube.com/channel/UCowfhbZ-yU3Db16nS-HNVEA)

## Setup guides

[Written guide](https://heygarethevans.notion.site/Setup-Instructions-e907297617104d5d850ca403922413cd)

[Video Guide](https://www.youtube.com/watch?v=7Yc06t7oY7s)

## Raspberry PI/cronjob setup

With this method we don't have to run the code locally on the device. We can also run it on a server or a raspberry pi

### Shell script

```
#!/bin/sh
# notion_crpto_updater.sh

cd /
cd /home/pi/Desktop/NotionCryptoPriceUpdater
python3 read.py
cd /
```

### Cronjob

Start editing crontab: `crontab -e`

```
@reboot sleep 30 &&  sh /home/pi/Desktop/NotionCryptoPriceUpdater/notion_crypto_updater.sh > /home/pi/Desktop/NotionCryptoPriceUpdater/script_logs/cronlog 2>&1
```

NOTE: `@reboot` is used to wait for the network connectivity to be active
