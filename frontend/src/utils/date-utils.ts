import moment from "moment";

const todayDate = () => {
  return moment().format("yyyy-MM-DD");
};

export { todayDate };
