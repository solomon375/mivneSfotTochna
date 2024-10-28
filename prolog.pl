/*Shlomo Salhoov 206787228*/

/********** PART A **********/
/***** question 1 *****/ 
parent(ELI,SHLOMO),male(ELI)
/***** question 2 *****/ 
parent(FANNY,SHLOMO),female(FANNY)
/***** question 3 *****/ 
son(SHLOMO,ELI):-parent(ELI,SHLOMO),male(SHLOMO)
/***** question 4 *****/ 
daughter(HODAYA,ELI):-parent(ELI,HODAYA),female(HODAYA)
/***** question 5 *****/ 
grandfather(SALIM,HODAYA):-parent(SALIM,FANNY),parent(FANNY,HODAYA),male(SALIM)
/***** question 6 *****/ 
grandmother(ZAKIA,HODAYA):-parent(ZAKIA,ELI),parent(ELI,HODAYA),female(ZAKIA)
/***** question 7 *****/ 
male_grandchild(SHLOMO,ZAKIA):-parent(ZAKIA,ELI),parent(ELI,SHLOMO),male(SHLOMO)
/***** question 8 *****/ 
female_grandchild(HODAYA,ZAKIA):-parent(ZAKIA,ELI),parent(ELI,HODAYA),female(HODAYA)
/***** question 9 *****/ 
sibling(HODAYA,SHLOMO):-parent(ELI,HODAYA),parent(ELI,SHLOMO)
/***** question 10 *****/ 
uncle_not_related(SHLOMO,MOTI)
/***** question 11 *****/ 
son_of_aunt(AMI,SHLOMO):-son(SHLOMO,ELI),sibling(ELI,MAZAL),son(AMI,MAZAL),female(MAZAL)
/***** question 12 *****/

/***** question 13 *****/ 
daughter_of_sibling(MIRYAM,SHLOMO):-daughter(MIRYAM,HODAYA),sibling(HODAYA,SHLOMO)
/***** question 14 *****/ 


/********** PART B **********/
/***** question 1 *****/ 

/***** question 2 *****/ 

/***** question 3 *****/ 

/***** question 4 *****/

/***** question 5 *****/ 


/********** PART C **********/
/***** question 1 *****/ 
/* part 1 */

/* part 2 */


/***** question 2 *****/ 
/* part 1 */

/* part 2 */

/* part 3 */


/***** question 3 *****/ 
/* part 1 */

/* part 2 */