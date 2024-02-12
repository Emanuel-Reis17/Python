// Easy and quick development tools 
class EasyDevTools {
    /**
     * Find any element
     * @param {Integer} num = Select one or more elements
     * @param {String} element = The element
     * @returns NodeList[...] or element
     */
    findElement = (num, element) => num === 0 ? document.querySelector(`${element}`) : document.querySelectorAll(`${element}`);

    /**
     * Capitalize text
     * @param {String} e = Text
     * @returns text capitalized
     */
    capitalize = e => {
        let phrase = e.trim().split(' ');
        return phrase.map(p => p.charAt(0).toUpperCase() + p.slice(1).toLowerCase()).join(' ');
    }

    /**
     * Create a HTML element
     * @param {String} el = The type of HTML element to create. It defaults to 'p' (paragraph).
     * @param {String} attr = The attribute to set. It defaults to 'id'.
     * @param {String} className = The value of the attribute to set. It defaults to 'paragraph'.
     * @param {String} container = The selector for the container where the new element will be appended. It defaults to 'body'.
     * @returns It returns true indicating that the operation was successful.
     */
    createElement = (el='p', attr='id', className='paragraph', container='body') => {
        const element = document.createElement(el);
        element.setAttribute(attr, className);
        document.querySelector(container).appendChild(element);
        return true;
    }
}
