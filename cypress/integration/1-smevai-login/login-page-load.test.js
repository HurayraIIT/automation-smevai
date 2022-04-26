/// <reference types="cypress" />

/**
 * Trying to see if the login page, 
 * registration page and forgot password 
 * page loads properly or not.
 */

const config = require('../../../util/config.json');

describe('Login Page Load Test', () => {
    beforeEach(() => {
        cy.visit(config.testing_site);
    });
    
    it('Test the main login page contents', () => {
        cy.contains('Phone Number / Email');
        cy.url().should('include', 'smevai.com/login');
    });
    
    it('Test the signup/register page contents', () => {
        // Go to the signup page and verify
        cy.contains('Signup').click();
        cy.url().should('include', 'smevai.com/register');
        cy.contains('Register');
        cy.contains('First Name');
        cy.contains('Already have an account?');
    });
    
    it('Test the forgot password page contents', () => {
        // Go to the forgot password page
        cy.contains('Forgot Password?').click();
        cy.url().should('include', 'smevai.com/password/reset');
        cy.contains('Forgot');
    });
});