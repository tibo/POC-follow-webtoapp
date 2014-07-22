//
//  ViewController.m
//  FollowApp
//
//  Created by Thibaut LE LEVIER on 21/07/2014.
//  Copyright (c) 2014 Thibaut LE LEVIER. All rights reserved.
//

#import "ViewController.h"
#import "SessionManager.h"
#import "APIClient.h"

@interface ViewController ()

@property (strong, nonatomic) IBOutlet UILabel *helloLabel;

@end

@implementation ViewController

#pragma mark - birth and death
- (void)dealloc
{
    [[SessionManager sharedSession] removeObserver:self forKeyPath:@"followKey"];
}

#pragma mark - view lifecycle
- (void)viewDidLoad
{
    [super viewDidLoad];
    
    [[SessionManager sharedSession] addObserver:self forKeyPath:@"followKey" options:NSKeyValueObservingOptionNew context:nil];
    
    NSURL *redirectURL = [NSURL URLWithString:[NSString stringWithFormat:@"%@/redirectToApp", SERVER_API_URL]];
    
    [[UIApplication sharedApplication] openURL:redirectURL];
}


#pragma mark - KVO
-(void)observeValueForKeyPath:(NSString *)keyPath ofObject:(id)object change:(NSDictionary *)change context:(void *)context
{
    if ([object isEqual:[SessionManager sharedSession]])
    {
        [APIClient getSessionForFollowKey:[SessionManager sharedSession].followKey
                             withCallback:^(NSDictionary *session, NSError *error) {
                                 
                                 if (error)
                                 {
                                     NSLog(@"Error : %@",error);
                                     UIAlertView *alert = [[UIAlertView alloc] initWithTitle:@"Error"
                                                                                     message:@"Session follow failed"
                                                                                    delegate:nil
                                                                           cancelButtonTitle:@"OK"
                                                                           otherButtonTitles:nil];
                                     [alert show];
                                 }
                                 else
                                 {
                                     [SessionManager sharedSession].login = [session objectForKey:@"login"];
                                     self.helloLabel.text = [NSString stringWithFormat:@"Hello\n%@",[SessionManager sharedSession].login];
                                 }
                                 
                                 
                             }];
    }
}


@end
