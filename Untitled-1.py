// ==UserScript==
// @name         Edge-nuity Megascript
// @version      2.3
// @description  Completes through instructional, summary, and warm-up sections by guessing answers (they don’t impact grades). You can begin activities while the instructor is speaking, when theres an activity, a "Search clipboard" button appears for quick access to answers during quizzes (will search your copied text on brainly and auto-redirect) And much more (read desc).
// @author       TTT
// @license MIT
// @include ://*nuity.com/*
// @include https://brainly.com/*
// @grant        none
// @namespace https://www.tampermonkey.net/
// @downloadURL https://update.greasyfork.org/scripts/515137/Edge-nuity%20Megascript.user.js
// @updateURL https://update.greasyfork.org/scripts/515137/Edge-nuity%20Megascript.meta.js
// ==/UserScript==
function redirectToStudent() {
    const currentHref = window.location.href;

    const newHref = currentHref.replace("core.learn", "student");

    window.location.href = newHref;
}

if (window.location.href.includes("core.learn") && window.location.href.includes("/EdgeAuth/lti/goodbye")) {

    setInterval(redirectToStudent, 1000);
}

function clickVisibleElementWithClass() {
    const elements = document.getElementsByClassName('btn btn-primary modal-dialog-button');

    for (let i = 0; i < elements.length; i++) {
        const targetElement = elements[i];
        const computedStyle = window.getComputedStyle(targetElement);
        const boundingRect = targetElement.getBoundingClientRect();

        const isVisible =
            computedStyle.opacity !== '0' &&
            computedStyle.visibility !== 'hidden' &&
            computedStyle.display !== 'none' &&
            boundingRect.width > 0 &&
            boundingRect.height > 0;

        if (isVisible) {
            const simulatedClickEvent = new MouseEvent('click', {
                view: window,
                bubbles: true,
                cancelable: true
            });
            targetElement.dispatchEvent(simulatedClickEvent);
            console.log('Clicked a visible button!');
            addBeforeUnloadListener();
            break;
        }
    }
}

setInterval(clickVisibleElementWithClass, 1000);

const checkElementVisibility = (element) => {
    const boundingRect = element.getBoundingClientRect();
    const computedStyle = window.getComputedStyle(element);
    return (
        computedStyle.opacity !== '0' &&
        computedStyle.visibility !== 'hidden' &&
        computedStyle.display !== 'none' &&
        boundingRect.width > 0 &&
        boundingRect.height > 0
    );
};

const checkForTimerStayElement = () => {
    const targetElement = document.getElementById('timerStay');

    if (targetElement && checkElementVisibility(targetElement)) {
        const simulatedClickEvent = new MouseEvent('click', {
            view: window,
            bubbles: true,
            cancelable: true
        });
        targetElement.dispatchEvent(simulatedClickEvent);
        console.log('Clicked timerStay element!');
        addBeforeUnloadListener();
    }
};

if (window.top === window.self) {
    const intervalId = setInterval(checkForTimerStayElement, 100);
}

const addBeforeUnloadListener = () => {
    window.onbeforeunload = function (event) {
        const message = 'Are you sure you want to leave this page?';
        event.returnValue = message;
        return message;
    };
};
let videoElement = null;
let alertTriggered = false;
let alertScheduled = false;

const callback = function(mutationsList, observer) {
  for (const mutation of mutationsList) {
    if (mutation.type === 'childList') {
      videoElement = document.getElementById("home_video_js");
      if (videoElement) {
        startCheckingVideo();

        observer.disconnect();
      }
    }
  }
};

const config = {
  attributes: false,
  childList: true,
  subtree: true
};

const targetNode = document.body;
const observer = new MutationObserver(callback);
observer.observe(targetNode, config);

function insertDiv() {
    let logoImage = document.querySelector('img.course-logo-bug[src="/images/logobug-edge-ex.png"][alt="Edge EX"]');
    if (logoImage && !document.getElementById('testDiv')) {

        const testDiv = document.createElement('div');
        testDiv.id = 'testDiv';
        testDiv.style.fontFamily = 'Atkinson Hyperlegible';
        testDiv.style.color = 'black';
        testDiv.style.margin = '10px';
        testDiv.style.width = 'calc(100% - 20px)';
        testDiv.style.maxWidth = '999px';
        testDiv.style.marginLeft = 'auto';
        testDiv.style.marginRight = 'auto';
        testDiv.style.position = 'fixed';
        testDiv.style.top = '50%';
        testDiv.style.left = '50%';
        testDiv.style.transform = 'translate(-50%, -50%)';
        testDiv.style.backgroundColor = 'aqua';
        testDiv.style.padding = '10px';
        testDiv.style.borderRadius = '5px';
        testDiv.style.zIndex = '2147483647';

        const firstItemContainer = document.createElement('div');

        const textSpan = document.createElement('span');
        textSpan.style.display = 'inline';
        textSpan.textContent = "Sadly, the script you downloaded (Edge-nuity Megascript) Does not support Edge-x classes, which you have one or more of. (Each marked by):";

        firstItemContainer.appendChild(textSpan);

        const imageContainer = document.createElement('span');
        imageContainer.style.display = 'inline';
        imageContainer.style.marginLeft = '10px';

        const imgElement1 = document.createElement('img');
        imgElement1.src = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACwAAAAsCAMAAAApWqozAAACSVBMVEUAAAAAAAAAAIAAAIAAAGYAAHEAAIAAAHQAAHcAAIAAAHkAAIAAAHkAAIAAAHoAAIAAAIAAAHsAAIAAAHsAAIAAAHwAAHwAAHkAAHwAAHkAAH0AAHoAAHoAAH0AAHsAAH0AAH0AAHsAAHsAAHwAAHoAAHsAAHwAAHsAAH0AAH0AAHsAAHwAAH0AAHsAAHwAAHwAAHwAAH0AAH0AAHwAAHsAAHwAAHsAAHwAAHwAAHwAAHwAAHwAAH0AAHwAAHsAAHwAAHwAAHsAAHwAAHwAAHwAAHwAAHwAAHwAAHwAAHwAAHwAAH0AAHsAAHwAAHsAAHwAAHsAAHwAAHwAAHwAAHwAAHwAAHwAAHwAAHwAAHwAAHwAAHwAAHwAAHwAAHwAAHwAAHwAAHwAAHwAAHwAAHwAAHwAAHwAAHwAAHwAAHwCAn0DA34EBH4FBX8GBn8NDYMQEIQREYUSEoUXF4gYGIgZGYkaGokhIY0jI44qKpIxMZU1NZc4OJk5OZk6Opo7O5o8PJs9PZtAQJ1DQ55ERJ9GRqBHR6BJSaFKSqJMTKNSUqZVVaheXqxmZrBnZ7FoaLFqarJsbLN3d7l6ert8fLyDg7+EhMCFhcCHh8GLi8OVlcmZmcudnc2fn86goM6hoc+ios+kpNCqqtOrq9StrdWvr9axsdezs9i2ttm3t9q6uty7u9zGxuLMzOXNzeXOzubS0ujU1OnV1enX1+rY2Ovm5vLt7fbw8Pfx8fjy8vjz8/n29vr39/v4+Pv5+fz6+vz9/f7+/v7///9aaBvrAAAAaXRSTlMAAQIEBQkKCw8QExQVGBkaHB0eHyIjJSYnKi0uMDM0NTc8PkhLTVJTWl5faWpub3uAg4uMmZqbnKSmp6ussba3vb7AwcPEx8jKy9TX29zd3t/g4ePl5+jp6uvv8PHy9PX29/j5+vv8/f5VPlHWAAAAAWJLR0TC/W++1AAAAixJREFUGBmNwYlDi3EcB+DvshZCh0hIEYlKhYjRnKEoSm6ion2Wlkju+0quotx3rsqR3BrZ9y/zvvu97/Zu7d32POQjZkbuso3bsGvz6rzM8QYKICK9AFrF2dGkIzxrK3xV5UaRPykl8GdHpoF8GWdboSM/kryZ8qGvZCxpRaxEIOXx5GG0ILD1UeQ2B8EUGEmRYkVQOSSEFyO4qgRyyUIoLCSL2IKQJJEkHaFZSJJVcKl/0N3j1nkSgr397U0Ie4YRxUB4zFp/rkBmf8PMLRDSiGZC6GUvjssA6l6z5D6EeURzIdxjb45LqHvFkn9nIBQRLYdgu/7wkaqXJf3NnSxx3oCi2khlcNvfIKkHcOADq5y34BZHO6Hq6GdZ3zGg4SMLzlZ4TKR9UBxnRReAg59Y5myDxmSqgOI8K94DqH3JsoFz0JhEm6Co7WYXx1XA9pyF32fhMY7WQGU7cVFyoRGwPWXVr9NQWU2UB48jLddcXrDs7meW/DwFRSnRLLg1/2WN2zjUx5IfRyGYiSbArYs17gBo/MKSDggZRIZiqJ6wRztkh78ycytcamKJKBuqpp4BFr61QWh69/2ZHS5LSBJdiZCkkiwXoSgMI9nI7QjBVBIyEZyZFIbFCKYsklQj1iGwimTyGFOOQPZOI624tdBXOZ28jVoBPaXJ5GtITjX8Mg8nPxIsGKwwhXQkLdgNrZqlqWGkb2ja/KJqyKwbFmXEUlDG0YlTEuNNNNh/Z1K0M41d9QQAAAAASUVORK5CYII=';
        imgElement1.alt = 'Embedded Image';
        imgElement1.style.maxHeight = '50px';

        imageContainer.appendChild(imgElement1);

        firstItemContainer.appendChild(imageContainer);

        testDiv.appendChild(firstItemContainer);

        const additionalInfoDiv = document.createElement('div');
        additionalInfoDiv.style.marginTop = '10px';
        additionalInfoDiv.textContent = "However, I'm gonna work on adding it as soon as possible, join ";

        const link = document.createElement('a');
        link.href = "https://discord.gg/6qJwkYSmrQ";
        link.target = "_blank";
        link.style.color = 'blue';
        link.style.textDecoration = 'underline';
        link.textContent = "HERE";

        additionalInfoDiv.appendChild(link);
        additionalInfoDiv.append(" and ping me \"@TallTacoTristan\" in any chat if you want to volunteer your own class, which I will complete for you in return.");

        testDiv.appendChild(additionalInfoDiv);

        const line3Div = document.createElement('div');
        line3Div.style.marginTop = '10px';
        line3Div.textContent = "If not, simply note: only normal classes are supported, any normal class is marked by:";

        const imageContainer2 = document.createElement('span');
        imageContainer2.style.display = 'inline';
        imageContainer2.style.marginLeft = '10px';
        const imgElement2 = document.createElement('img');
        imgElement2.src = 'data:image/png;base64,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
