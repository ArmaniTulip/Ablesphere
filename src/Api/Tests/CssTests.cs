using Xunit;

namespace Api.Tests
{
    public class CssTests
    {
        [Fact]
        public void CssFile_ShouldExist()
        {
            // Arrange
            var cssFilePath = "src/Api/wwwroot/css/styles.css";

            // Act
            var fileExists = System.IO.File.Exists(cssFilePath);

            // Assert
            Assert.True(fileExists, "CSS file should exist.");
        }

        [Fact]
        public void CssFile_ShouldContainResponsiveStyles()
        {
            // Arrange
            var cssFilePath = "src/Api/wwwroot/css/styles.css";
            var cssContent = System.IO.File.ReadAllText(cssFilePath);

            // Act
            var containsResponsiveStyles = cssContent.Contains("@media (max-width: 768px)");

            // Assert
            Assert.True(containsResponsiveStyles, "CSS file should contain responsive styles.");
        }
    }
}