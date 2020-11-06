const wait = async (millisec: number) => {
  return new Promise((resolve) => {
    setTimeout(() => resolve(), millisec);
  })
}

export default wait