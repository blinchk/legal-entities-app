const generateRegistryCode = () => {
  return new Promise<string>((resolve, reject) => {
    return fetch("http://localhost:8000/legal-entity/registry-code")
      .then((response) => response.json())
      .then((data) => resolve(data));
  });
};

export { generateRegistryCode };
