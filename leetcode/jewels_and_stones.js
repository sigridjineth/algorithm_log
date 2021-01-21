// LEETCODE 771 Jewels and Stones 보석과 돌
// Implementing DefaultDict of Python in JavaScript
class DefaultMap extends Map {
    constructor(getDefaultValue, ...mapConstructorArgs) {
        super(mapConstructorArgs);
        
        if (typeof getDefaultValue !== 'function') {
            throw new Error('getDefaultValue must be a function');
        };

        this.getDefaultValue = getDefaultValue;
    }

    get = key => {
        if (!this.has(key)) {
            this.set(key, this.getDefaultValue(key));
        };
        return super.get(key);
    };
};

solution = (J, S) => {
    freqs = new DefaultMap(() => 0);
    count = 0;

    for (let char of S) {
        freqs.set(char, freqs.get(char) + 1);
    };

    for (let char of J) {
        count += freqs.get(char);
    };

    return count;
};

console.log(solution("aA", "aAAbbbb"))