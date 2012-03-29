# Marcus M. Darden -- 2012-02-28
# rps.asm: A rock-paper-scissors game in assembly language
# Registers:
#	$s0 -	Computer weapon
#	$s1 -	Player weapon
#	$t0 -	Temp value
#	$t1 -	String argument (outcome)
#	$v0 -	syscall parameter
#	$a0 -	Function argument (string address for print_string)

	.text
main:						# Execution begins here
	## Print intro
	la	$a0, msg_intro			# Get address of intro message
	li	$v0, 4				# print_string syscall parameter
	syscall					# Execute syscall

	## Generate computer weapon
	jal	get_random			# Generate a random 32-bit integer
	move	$s0, $v0			# s0 = v0
	li	$t0, 3				# t1 = 3
	divu	$s0, $t0			# s0 / t0  or  s0 / 3
	mfhi	$s0				# Computer weapon in t0
	addi	$s0, $s0, 1			# Adjust to 1-3 range similar to user
	
	## Get user weapon
	li	$v0, 5				# read_int syscall parameter
	syscall					# Execute syscall
	move	$s1, $v0			# Player weapon in s1

	## Determine results (Computer in s0, player in s1)
	beqz	$s1, the_end			# User wants to quit, do it
	beq	$s0, $s1, tie			# s0 == s1, game is a tie
	beq	$s0, 2, paper			# Computer weapon is paper
	beq	$s0, 3, scissors		# Computer weapon is scissors
						# Fall through to
						# Computer weapon is rock

	## rock here
	la	$a0, msg_crock			# Load computer rock message
	beq	$s1, 2, player_win		# Computer rock against paper
	b	computer_win			# Computer rock against scissors
paper:	
	## paper here
	la	$a0, msg_cpaper			# Load computer paper message
	beq	$s1, 3, player_win		# Computer paper against scissors
	b	computer_win			# Computer paper against rock
scissors:
	## scissors here
	la	$a0, msg_cscissors		# Load computer scissors message
	beq	$s1, 1, player_win		# Computer scissors against rock
						# Fall through to 
						# Computer scissors against paper
	
computer_win:
	la	$t1, msg_cwin			# Load computer wins message
	b	display_results			# Display
player_win:
	la	$t1, msg_pwin			# Load player wins message
	b	display_results			# Display
tie:
	la	$a0, msg_draw			# Load tie message
	b	display_tie			# Display

display_results:	# $a0 has computer weapon, $t1 has W/L result
	## Full results has computer choice (here) and outcome (next)
	li	$v0, 4				# print_string syscall parameter
	syscall					# Execute syscall
	move	$a0, $t1			# Outcome message
display_tie:
	## Tie results only display outcome
	li	$v0, 4				# print_string syscall parameter
	syscall					# Execute syscall
	b	main				# Loop game

the_end:
	la	$a0, msg_goodbye		# Location of goodbye message
	li	$v0, 4				# print_string syscall parameter
	syscall					# Execute syscall
	li	$v0, 10				# exit syscall parameter
	syscall					# Execute syscall


	.data
msg_intro:		.ascii "\nPlay Rock-Paper-Scissors\n"
			.asciiz "Choose your weapon? (1=Rock, 2=Paper, 3=Scissors, 0 to quit) "
msg_crock:		.asciiz "Computer used rock, "
msg_cpaper:		.asciiz "Computer used paper, "
msg_cscissors:		.asciiz "Computer used scissors, "
msg_cwin:		.asciiz "Computer wins!\n"
msg_pwin:		.asciiz "Player wins!\n"
msg_draw:		.asciiz "That's what the Computer used, it's a tie.\n"
msg_goodbye:		.asciiz "Goodbye!\n"
