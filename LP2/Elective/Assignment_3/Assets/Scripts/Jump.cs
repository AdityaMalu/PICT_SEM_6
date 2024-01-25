using UnityEngine;

public class BouncingBall : MonoBehaviour
{
    public float speed = 5f;
    private Vector3 direction = Vector3.zero; // Initial direction is zero

    void Update()
    {
        // Check for space bar input to bounce the ball and start moving
        if (Input.GetKeyDown(KeyCode.Space))
        {
            Bounce();
            direction = new Vector3(0, 1, 0); // Start moving in the diagonal direction on space bar press
        }

        // Move the ball in the specified direction only when direction is not zero
        if (direction != Vector3.zero)
        {
            transform.Translate(direction * speed * Time.deltaTime);

            // Check if the ball has hit the screen bounds
            // CheckScreenBounds();
        }
    }

    // void CheckScreenBounds()
    // {
    //     // Get the screen bounds
    //     float screenBoundsX = Camera.main.orthographicSize * Screen.width / Screen.height;
    //     float screenBoundsY = Camera.main.orthographicSize;

    //     // Check if the ball has hit the screen bounds and change direction accordingly
    //     if (transform.position.x > screenBoundsX || transform.position.x < -screenBoundsX)
    //     {
    //         direction.x *= -1; // Reverse the x direction
    //     }

    //     if (transform.position.y > screenBoundsY || transform.position.y < -screenBoundsY)
    //     {
    //         direction.y *= -1; // Reverse the y direction
    //     }
    // }

    void Bounce()
    {
        // Reverse the y direction to simulate bouncing
        direction.y *= -1;
    }
}
