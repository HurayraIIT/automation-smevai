"use strict";
const {Builder, By, Key, until} = require('selenium-webdriver');
const config = require('./util/config.json');

async function example() {
    const driver = await new Builder().forBrowser('firefox').build();
    await driver.get(config.live_site);
    await driver.findElement(By.name('username')).sendKeys(config.email, Key.RETURN);
    await driver.findElement(By.name('password')).sendKeys(config.password, Key.RETURN);
    
}

example();