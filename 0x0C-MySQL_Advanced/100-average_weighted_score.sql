-- SQL script that creates a stored procedure
-- ComputeAverageWeightedScoreForUsers that computes and
-- store the average weighted score for all students.
-- Procedure ComputeAverageScoreForUser is taking 1 input:
-- user_id, a users.id value (you can assume user_id is linked to an existing users)

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    UPDATE users AS User, 
        (SELECT User.id, SUM(score * weight) / SUM(weight) AS w_avg 
        FROM users AS User 
        JOIN corrections as Cor ON User.id=Cor.user_id 
        JOIN projects AS Pj ON Cor.project_id=Pj.id 
        GROUP BY User.id)
    AS W_Average
    SET User.average_score = W_Average.w_avg
    WHERE User.id=W_Average.id;
END
//
DELIMITER ;