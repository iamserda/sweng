async function getApiData(){
    const apiUrl = "https://raw.githubusercontent.com/public-apis-dev/public-apis/main/db/resources.json"
    try{
        const response = await fetch(apiUrl,
            {
                "headers": {
                    "accept-language": "en-US,en;q=0.9",
                    "sec-ch-ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": "\"macOS\"",
                    "Referer": "https://free-apis.github.io/"
                },
                "body": null,
                "method": "GET"
            });
        if (!response.ok) {
            throw new Error(`Response status: ${response.status}`);
        }
        const data = await response.json()
        const entries = await data.entries
        for(let i=0; i<10; i++){
            console.log(entries[i])
        }
    }catch(err){
        console.error(err)
    }
    
}

getApiData()