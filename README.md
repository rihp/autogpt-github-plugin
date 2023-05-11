# AutoGPT Github Plugin
Simple github commands for autogpt.



### Getting started

After you clone the plugin from the original repo (https://github.com/rihp/autogpt-gihub-plugin) Add it to the plugins folder of your AutoGPT repo and then run AutoGPT

![image](https://user-images.githubusercontent.com/12145726/235688224-7abf6ae4-5c0a-4e2d-b1b2-18241c6d74b4.png)

Remember to also update your .env to include 

```
ALLOWLISTED_PLUGINS=GithubPlugin
```



# New commands
```python

prompt.add_command(
    "autogpt_github_status",
    "Fetches the status of the Auto-GPT repository, including forks, stars, and issues.",
    {},
    autogpt_github_status,
)
```



## Testing workflow

Clone the repo and modify the functionality, when you're done you can run 
```
zip -ru ../fork/plugins/github.zip . ; cd ../fork && python3 -m autogpt --debug 
```

then you need to cd back to 
```
cd ../autogpt-github-plugin    
```
