export const generateUserId = (length: number = 8): string => {
    const characters = 'abcdefghijklmnopqrstuvwxyz0123456789';
    let result = '';
    for (let i = 0; i < length; i++) {
      result += characters.charAt(Math.floor(Math.random() * characters.length));
    }
    return result;
  };
  
  export const getUserId = (): string => {
    const storedUserId = localStorage.getItem('userId');
    if (storedUserId) {
      return storedUserId;
    }
    
    const newUserId = generateUserId();
    localStorage.setItem('userId', newUserId);
    return newUserId;
  };
  
  export const resetUserId = (): string => {
    const newUserId = generateUserId();
    localStorage.setItem('userId', newUserId);
    return newUserId;
  };