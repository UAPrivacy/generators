const axios = require("axios");
const SAMPLE_DATA = require("./data");
const { DIFFBOT } = require("../secrets.json");
const { createQueryString } = require("./utils");

const ENDPOINT_URL = "https://api.diffbot.com/v3/article";

async function fetchText(url) {
  const options = {
    token: DIFFBOT,
    url
  };
  const { data } = await axios.get(
    `${ENDPOINT_URL}?${createQueryString(options)}`
  );

  return data.objects[0].text;
}

async function main() {
  for (const { website, url } of SAMPLE_DATA) {
    const text = await fetchText(url);
    console.log(`${website} > data \n`);
    console.log(text);
  }
}

main();
