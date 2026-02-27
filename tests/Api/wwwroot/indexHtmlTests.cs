using System;
using System.IO;
using System.Threading.Tasks;
using Xunit;

namespace Api.Tests.wwwroot
{
    public class IndexHtmlTests
    {
        private const string FilePath = "../../../src/Api/wwwroot/index.html";

        [Fact]
        public async Task IndexHtml_ShouldNotContainSyntaxErrors()
        {
            string htmlContent = await File.ReadAllTextAsync(FilePath);
            Assert.False(string.IsNullOrWhiteSpace(htmlContent), "HTML content should not be empty.");
            Assert.Contains("<!DOCTYPE html>", htmlContent, StringComparison.OrdinalIgnoreCase);
            Assert.Contains("<html lang=\"en\">", htmlContent, StringComparison.OrdinalIgnoreCase);
        }

        [Fact]
        public async Task IndexHtml_LinksShouldBeValid()
        {
            string htmlContent = await File.ReadAllTextAsync(FilePath);
            Assert.Contains("/css/styles.css", htmlContent, "Stylesheet link should be present.");
            Assert.Contains("/docs/endpoint1", htmlContent, "Endpoint 1 link should be present.");
            Assert.Contains("/docs/endpoint2", htmlContent, "Endpoint 2 link should be present.");
            Assert.Contains("/docs/endpoint3", htmlContent, "Endpoint 3 link should be present.");
        }
    }
}