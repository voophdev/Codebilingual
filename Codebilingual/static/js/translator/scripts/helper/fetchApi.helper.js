import { apiKEY, apiURL } from "../variables/variables.js";

const fetchApi = async ({ code }) => {
  const response = await fetch(apiURL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${apiKEY}`,
    },
    body: JSON.stringify({
      model: "gpt-4",
      messages: [{ role: "user", content: code }],
    }),
  });
  const body = await response.json();
  return body;
};

export { fetchApi };
