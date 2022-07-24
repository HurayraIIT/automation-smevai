/// <reference types="cypress" />

describe('First Test', () => {
  it('Visits the login page', () => {
    cy.visit("https://app.smevai.com/")
    
    cy.contains('Login')
    
    cy.url()
    .should('include', 'login')
    
    // cy.get('#password-field').type(1)
    // cy.get('/html/body/div/div[1]/div[2]/form/div[1]/input').click()
    
  })
})