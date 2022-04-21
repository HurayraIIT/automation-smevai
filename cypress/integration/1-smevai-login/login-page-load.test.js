/// <reference types="cypress" />

/**
 * Trying to see if the login page, 
 * registration page and forgot password 
 * page loads properly or not.
 */
describe('Login Page Load Test', () => {
    it('Login Page', () => {
        cy.visit('https://app.smevai.com')
        cy.contains('Phone Number / Email')
        cy.url().should('include', 'smevai.com/login')
        
        // Go to the signup page and verify
        cy.contains('Signup').click()
        cy.url().should('include', 'smevai.com/register')
        cy.contains('Register')
        cy.contains('First Name')
        cy.contains('Already have an account?')
        
        // Go back to the login page
        cy.go('back')
        cy.url().should('include', 'smevai.com/login')
        
        // Go to the forgot password page
        cy.contains('Forgot Password?').click()
        cy.url().should('include', 'smevai.com/password/reset')
        cy.contains('Forgot')
        
        // Go back to the login page
        cy.go('back')
        cy.url().should('include', 'smevai.com/login')
        
    })
})