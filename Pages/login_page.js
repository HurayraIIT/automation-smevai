/**
 * This class is responsible for the login
 * functionality testing.
 */

"use strict";
const { Builder, By, Key, until } = require('selenium-webdriver');
const config = require('../util/config.json');

class LoginPage {
    constructor(driver) {
        this.driver = driver;
    }

    async login() {
        await this.driver.get(config.site_to_test);
        await this.driver.findElement(By.name('username')).sendKeys(config.trading_admin_email, Key.RETURN);
        await this.driver.findElement(By.name('password')).sendKeys(config.password, Key.RETURN);
    }
}

module.exports = LoginPage;