#' Function Title
#'
#' The description of the function
#'
#' @param param1 Description of the first parameter (if any)
#' @param param2 Description of the second parameter (if any)
#' @return Description of the return value
#'
#' @examples
#' func1(1,2)
#'
#' @seealso func2, func3
#'
#' @author Anne Appleby
#' @author Barry Barsden
func1 <- function(param1 = "world", param2 = "!") {
  paste0("Hello ", param1, param2)
}
