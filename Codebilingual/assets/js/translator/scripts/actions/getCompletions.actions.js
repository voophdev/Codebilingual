import { fetchApi } from "../helper/fetchApi.helper.js";

const getCompletions = async ({ code }) => {
  const response = await fetchApi({ code: code });
  return response?.choices[0]?.message?.content.replace("\n", "");
};

export { getCompletions };
